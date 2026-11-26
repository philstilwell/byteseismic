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


def command(action, day):
    args = [sys.executable, str(ROOT / 'scripts/editorial_daily_gate.py'), action,
            '--date', day]
    if action == 'check':
        args += ['--phase', 'published']
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
    path = home / 'controller-sessions' / (session + '.json')
    state = json.loads(path.read_text()) if path.exists() else None
    prompt = payload.get('prompt', '')
    # Desktop scheduled messages can prepend an automation name/memory header.
    starts = event == 'UserPromptSubmit' and MARKER in prompt.splitlines()[:32]
    if not state and not starts:
        return {}  # Other conversations in the same repository are unaffected.
    if event == 'Interrupt':
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
                pending.append(previous['date'])
        day = min(pending) if pending else now.date().isoformat()
        state = {'sessionId': session, 'root': str(root), 'date': day,
                 'status': 'active', 'continuations': 0, 'updatedAt': now.isoformat()}
        save(path, state)  # Bind before planning, including when planning fails.
        code, output = run('plan', day)
        if code:
            context = 'Daily assignment planning failed; repair it before reviewing: ' + output
        else:
            context = f'Automatic continuation controller armed for {day}. Use that saved assignment date throughout this run.'
        return {'hookSpecificOutput': {'hookEventName': 'UserPromptSubmit',
                                      'additionalContext': context}}
    if event != 'Stop':
        return {}
    code, output = run('check', state['date'])
    state.update(updatedAt=now.isoformat(), lastCheck=output)
    if code == 0:
        state['status'] = 'complete'
        save(path, state)
        # A later scheduled run may recover an older failed session's assignment.
        # Retire that older binding too, so tomorrow does not reopen the same day.
        for other in (home / 'controller-sessions').glob('*.json'):
            previous = json.loads(other.read_text())
            if (previous.get('status') == 'active' and previous.get('date') == state['date']
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
        f"Automatic editorial continuation {state['continuations']} for {state['date']}. "
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
