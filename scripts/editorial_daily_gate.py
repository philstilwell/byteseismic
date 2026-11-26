#!/usr/bin/env python3
"""Persist the daily assignment and reject incomplete editorial finalization.

This checks recorded evidence, not the quality of human/editorial judgment.
It does not control the scheduler or automatically restart an interrupted process.
"""
import argparse
import hashlib
import json
import subprocess
import revise_source_conversations as conversations
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = Path('quality/original-source-revisions')


def read(root, path):
    return json.loads((root / path).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def records(root, day):
    result = {}
    for path in sorted((root / 'quality').glob(f'editorial-audit-{day}*.json')):
        for row in read(root, path).get('pages', []):
            verification = row.get('verification', {})
            page = verification.get('pagePath')
            if page and verification.get('sha256'):
                result[page] = (row, str(path.relative_to(root)))
    return result


def assignment(root, day):
    path = Path(f'quality/editorial-runs/{day}.json')
    if (root / path).exists():
        return read(root, path), path
    tracker = read(root, 'quality/editorial-audit-tracker.json')
    if tracker['cursor']['cycle'] != 8:
        raise ValueError('Only the authorized cycle 8 is supported; do not restart.')
    queue = [x['pagePath'] for x in tracker['pages']]
    done = set(tracker['cursor']['completedPagePathsInCurrentCycle'])
    for progress in (root / DATA).glob('current-batch-progress-*.json'):
        data = read(root, progress)
        if data.get('cycle') == 8:
            done.update(x['pagePath'] for x in data['pages']
                        if x['status'] == 'reviewed-and-verified')
    today = set(records(root, day))
    if today - set(queue):
        raise ValueError('Today’s records include pages outside the authorized queue.')
    if len(today) > 20:
        raise ValueError('More than twenty recorded pages: reconcile before planning.')
    remaining = [x for x in queue if x not in done and x not in today]
    selected = [x for x in queue if x in today] + remaining[:20-len(today)]
    plan = {'date': day, 'timezone': 'America/New_York', 'cycle': 8,
            'target': len(selected), 'pagePaths': selected,
            'remainingAtPlanning': len(remaining) + len(today),
            'endpointException': len(selected) < 20}
    (root / path).parent.mkdir(parents=True, exist_ok=True)
    (root / path).write_text(json.dumps(plan, indent=2, ensure_ascii=False) + '\n')
    return plan, path


def evidence(root, plan):
    """Return problems and the exact files whose committed contents are required."""
    errors, files = [], set()
    pages = plan['pagePaths']
    target = min(20, plan['remainingAtPlanning'])
    if len(pages) != len(set(pages)) or len(pages) != target or plan['target'] != target:
        return ['Daily assignment has duplicate pages or an incorrect target.'], files
    today = records(root, plan['date'])
    tracked = set()
    for progress_path in (root / DATA).glob('current-batch-progress-*.json'):
        progress = read(root, progress_path)
        if progress.get('cycle') != plan.get('cycle', 8):
            continue
        relevant = [x for x in progress['pages'] if x['pagePath'] in pages]
        if relevant:
            files.add(str(progress_path.relative_to(root)))
            tracked.update(x['pagePath'] for x in relevant
                           if x['status'] == 'reviewed-and-verified')
    if set(pages) - tracked:
        errors.append('Assigned pages are missing verified partial-batch progress.')
    files.update(['quality/editorial-audit-tracker.json',
                  'scripts/revise_source_conversations.py'])
    build_path = DATA / f"batch-verification-{plan['date']}.json"
    files.add(str(build_path))
    try:
        build = read(root, build_path)['build']
        if build.get('isolated') is not True or not build.get('log'):
            errors.append('Missing isolated full-build evidence.')
        hashes = build.get('reviewedPageHashes', {})
    except (OSError, KeyError, ValueError):
        errors.append(f'Missing or invalid full-build record: {build_path}')
        hashes = {}
    for page in pages:
        try:
            row, report = today[page]
            slug = page.strip('/').split('/')[-1]
            config_path = DATA / f'{slug}-edits.json'
            verification_path = DATA / f"{slug}-verification-{plan['date']}.json"
            config = read(root, config_path)
            verification = read(root, verification_path)
            article = page.strip('/') + '/index.html'
            source = DATA / config['snapshot']
            files.update(map(str, [report, config_path, verification_path, article, source]))
            if not row.get('decisions') or not row.get('source'):
                raise ValueError('missing individual editorial decisions/source')
            if verification['pagePath'] != page or config['pageFile'] != article:
                raise ValueError('page identity mismatch')
            for key in ['promptOrderExact', 'sourceBlockOrderExact', 'sourceCacheExact',
                        'sourceUrlMatched', 'rendererReproduces', 'isolatedBuildVerified']:
                if verification.get(key) is not True:
                    raise ValueError(f'{key} is not verified')
            if not verification.get('damagedVariantsRejected'):
                raise ValueError('missing negative fidelity checks')
            coverage = verification['sourceReadingCoverage']
            covered = {i for a, b in coverage['ranges'] for i in range(a, b+1)}
            if not set(range(1, coverage['indexedLines']+1)) <= covered or coverage['indexedLines'] < 1:
                raise ValueError('incomplete source-reading coverage')
            digest = sha(root / article)
            if digest != verification['sha256'] or digest != hashes.get(page):
                raise ValueError('current page does not match fidelity and build hashes')
            if sha(root / source) != verification['sourceSha256'] or config['sourceSha256'] != verification['sourceSha256']:
                raise ValueError('source snapshot hash mismatch')
            if row['verification']['sha256'] != digest:
                raise ValueError('daily report refers to a different page version')
            # The existing verifier explicitly records legitimate list splits and
            # appendices as structure changes. Revalidate them, never demand an
            # inaccurate "unchanged" flag or accept a blanket exception.
            actual = conversations.verify(config, (root / article).read_text())
            for key in ['listAndTableStructuresPreserved', 'explicitListItemSplits',
                        'explicitResponseAppendices', 'formatChecks', 'sha256']:
                if actual[key] != verification[key]:
                    raise ValueError(f'recorded {key} differs from live fidelity verification')
        except (OSError, ValueError, KeyError, TypeError, AssertionError) as exc:
            errors.append(f'{page}: {exc}')
    return errors, files


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root, text=True).strip()


def publication(root, files):
    errors = []
    for path in sorted(files):
        try:
            git(root, 'ls-files', '--error-unmatch', '--', path)
            if git(root, 'diff', 'HEAD', '--', path):
                errors.append(f'Uncommitted evidence or content: {path}')
        except subprocess.CalledProcessError:
            errors.append(f'Untracked evidence or content: {path}')
    try:
        local = git(root, 'rev-parse', 'HEAD')
        remote = git(root, 'ls-remote', 'origin', 'refs/heads/main').split()
        if not remote or local != remote[0]:
            errors.append('Local commit is not confirmed on origin/main; finish the push.')
    except subprocess.CalledProcessError:
        errors.append('Remote push verification failed; retry or document the actual blocker.')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['plan', 'check'])
    parser.add_argument('--date', default=datetime.now(ZoneInfo('America/New_York')).date().isoformat())
    parser.add_argument('--phase', choices=['ready', 'published'], default='published')
    args = parser.parse_args()
    date.fromisoformat(args.date)
    plan_path = Path(f'quality/editorial-runs/{args.date}.json')
    if args.action == 'plan':
        plan, _ = assignment(ROOT, args.date)
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return 0
    if not (ROOT / plan_path).exists():
        print('CONTINUE: create the daily assignment with the plan command first.')
        return 1
    plan = read(ROOT, plan_path)
    errors, files = evidence(ROOT, plan)
    files.add(str(plan_path))
    if args.phase == 'published' and not errors:
        errors.extend(publication(ROOT, files))
    if errors:
        print('CONTINUE — daily completion check failed:')
        print('\n'.join('- ' + error for error in errors))
        return 1
    if args.phase == 'ready':
        print(f"READY: {plan['target']} pages verified. Commit and push, then run the published check; do not finalize yet.")
    else:
        print(f"COMPLETE: {plan['target']}/{plan['target']} pages verified, committed and remote push confirmed.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
