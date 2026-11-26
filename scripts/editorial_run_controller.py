#!/usr/bin/env python3
"""Codex lifecycle controller: an incomplete Stop becomes a new model turn.

Called by trusted project hooks, not by the editorial agent. Only automation
prompts with MARKER activate it. A user interrupt always suspends continuation.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import tomllib
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

MARKER = '[byteseismic-editorial-controller:v1]'
AUTOMATION = 'byteseismic-daily-editorial-audit'
ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home() / '.codex/automations' / AUTOMATION


def scheduled_prompt(payload, root):
    """Recover the scheduler's tool-delivered prompt from the hook's transcript.

    Desktop automation turns do not necessarily emit UserPromptSubmit. Read only
    the runtime-provided transcript, require matching session metadata, and accept
    only the scheduler's named automation_update output, never arbitrary text.
    """
    name = payload.get('transcript_path')
    if not name:
        return None
    budget = 16 * 1024 * 1024
    matched_session = False
    with Path(name).open() as transcript:
        for _ in range(128):
            line = transcript.readline(min(budget + 1, 2 * 1024 * 1024))
            if not line:
                break
            budget -= len(line.encode())
            if budget < 0 or not line.endswith('\n'):
                break
            item = json.loads(line)
            data = item.get('payload', {})
            if item.get('type') == 'session_meta':
                matched_session = (data.get('id') == payload.get('session_id')
                                   and data.get('thread_source') == 'automation'
                                   and Path(data.get('cwd', '/')).resolve() == root.resolve())
            if (matched_session and item.get('type') == 'response_item'
                    and data.get('type') == 'function_call_output'
                    and data.get('namespace') == 'codex_app'
                    and data.get('name') == 'automation_update'):
                text = data.get('output', '')
                if (isinstance(text, str) and f'Automation ID: {AUTOMATION}' in text.splitlines()[:8]
                        and MARKER in text.splitlines()[:32]):
                    return text
    return None


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix='.controller-')
    try:
        with os.fdopen(fd, 'w') as handle:
            json.dump(data, handle, indent=2)
            handle.write('\n')
        os.replace(name, path)
    finally:
        if Path(name).exists():
            Path(name).unlink()


def command(action, day, run_id=None):
    args = [sys.executable, str(ROOT / 'scripts/editorial_daily_gate.py'), action,
            '--date', day]
    if action == 'check':
        args += ['--phase', 'published']
    if run_id:
        args += ['--run-id', run_id]
    # A network stall must not hang the stop hook indefinitely or pass as success.
    process = subprocess.Popen(args, cwd=ROOT, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, text=True,
                               start_new_session=True)
    try:
        output, _ = process.communicate(timeout=45)
        return process.returncode, output[-6000:]
    except subprocess.TimeoutExpired:
        import signal
        os.killpg(process.pid, signal.SIGKILL)
        process.communicate()
        return 1, 'Completion verification timed out. Resolve the operation and retry.'


def handle(payload, home=HOME, root=ROOT, run=command, now=None):
    now = now or datetime.now(ZoneInfo('America/New_York'))
    if Path(payload.get('cwd', '/')).resolve() != root.resolve():
        return {}
    session = payload.get('session_id', '')
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,100}', session):
        return {}
    event = payload.get('hook_event_name')
    observation_path = home / 'controller-hook-observations.json'
    observations = json.loads(observation_path.read_text()) if observation_path.exists() else []
    observations.append({'sessionId': session, 'event': event, 'time': now.isoformat(),
                         'payloadKeys': sorted(payload),
                         'transcriptPath': payload.get('transcript_path')})
    save(observation_path, observations[-32:])
    path = home / 'controller-sessions' / (session + '.json')
    state = json.loads(path.read_text()) if path.exists() else None
    prompt = payload.get('prompt', '')
    recovered = False
    if not state and event in ['Stop', 'Interrupt']:
        recovered_prompt = scheduled_prompt(payload, root)
        if recovered_prompt:
            prompt = recovered_prompt
            recovered = True
    # Desktop scheduled messages can prepend an automation name/memory header.
    starts = (event == 'UserPromptSubmit' or recovered) and MARKER in prompt.splitlines()[:32]
    if not state and not starts:
        return {}  # Other conversations in the same repository are unaffected.
    if event == 'Interrupt':
        if not state and recovered:
            state = {'sessionId': session, 'root': str(root),
                     'date': now.date().isoformat(), 'continuations': 0}
        if state:
            state.update(status='user-interrupted', updatedAt=now.isoformat())
            save(path, state)
        return {}
    config = tomllib.loads((home / 'automation.toml').read_text())
    if config['status'] != 'ACTIVE':
        return {}  # Pausing the automation also disables automatic continuation.
    if state and state['status'] in ['complete', 'user-interrupted']:
        return {}
    if starts and not state:
        # Recover a prior unfinished date; never shift an assignment at midnight.
        pending = []
        for other in (home / 'controller-sessions').glob('*.json'):
            previous = json.loads(other.read_text())
            if previous.get('status') == 'active' and previous.get('root') == str(root):
                pending.append((previous['date'], previous.get('runId') or ''))
        explicit_runs = [m.group(1) for line in prompt.splitlines()[:32]
                         if (m := re.fullmatch(r'\[byteseismic-run:([a-z0-9][a-z0-9-]{0,39})\]', line))]
        if len(explicit_runs) > 1:
            raise ValueError('Ambiguous additional assignment.')
        if explicit_runs:
            day, run_id = now.date().isoformat(), explicit_runs[0]
        else:
            day, run_id = min(pending) if pending else (now.date().isoformat(), '')
        state = {'sessionId': session, 'root': str(root), 'date': day,
                 'status': 'active', 'continuations': 0, 'updatedAt': now.isoformat()}
        if run_id:
            state['runId'] = run_id
        save(path, state)  # Bind before planning, including when planning fails.
        code, output = run('plan', day, run_id) if run_id else run('plan', day)
        if code:
            context = 'Daily assignment planning failed; repair it before reviewing: ' + output
        else:
            context = f'Automatic continuation controller armed for {day}' + (f' --run-id {run_id}' if run_id else '') + '. Use that saved assignment throughout this run.'
        if not recovered:
            return {'hookSpecificOutput': {'hookEventName': 'UserPromptSubmit',
                                          'additionalContext': context}}
    if event != 'Stop':
        return {}
    run_id = state.get('runId')
    code, output = run('check', state['date'], run_id) if run_id else run('check', state['date'])
    state.update(updatedAt=now.isoformat(), lastCheck=output)
    if code == 0:
        state['status'] = 'complete'
        save(path, state)
        # A later scheduled run may recover an older failed session's assignment.
        # Retire that older binding too, so tomorrow does not reopen the same day.
        for other in (home / 'controller-sessions').glob('*.json'):
            previous = json.loads(other.read_text())
            if (previous.get('status') == 'active' and previous.get('date') == state['date']
                    and previous.get('runId') == state.get('runId')
                    and previous.get('root') == str(root)):
                previous.update(status='complete', completedBy=session,
                                updatedAt=now.isoformat())
                save(other, previous)
        return {'systemMessage': 'Editorial controller: verification and remote push confirmed; run complete.'}
    state['continuations'] += 1
    save(path, state)
    # Deliberately do NOT exit when stop_hook_active is true. Every premature
    # finish must be checked, including the second, third and later attempts.
    return {'decision': 'block', 'reason': (
        f"Automatic editorial continuation {state['continuations']} for {state['date']}" +
        (f" --run-id {run_id}. " if run_id else '. ') +
        'The controller independently checked the assignment and it is unfinished. '
        'Resume the first incomplete step now, without asking the user to continue. '
        'Complete every assigned original-source review, fidelity verification, isolated build, '
        'commit and confirmed push. Preserve the frozen assignment and original quality requirements. '
        'Do not modify or disable the controller/checker to end this run. '
        'Repair recoverable errors and preserve exact progress across compaction.\n\n' + output)}


def main():
    payload = json.load(sys.stdin)
    try:
        result = handle(payload)
    except Exception as exc:
        # The configured onFailure=block covers process failures too. Never turn
        # an exception in an armed Stop into an apparent successful completion.
        print(f'Editorial controller error: {type(exc).__name__}: {exc}. '
              'Repair verification and continue the saved assignment.', file=sys.stderr)
        return 2
    print(json.dumps(result))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
