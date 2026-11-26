import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from unittest.mock import Mock

import editorial_run_controller as controller


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / 'automation'
        self.home.mkdir()
        (self.home / 'automation.toml').write_text('status = "ACTIVE"\n')
        self.clock = datetime(2026, 11, 27, 9, tzinfo=ZoneInfo('America/New_York'))
        self.run = Mock(return_value=(0, 'assignment planned'))

    def event(self, name, **extra):
        payload = {'cwd': str(self.root), 'session_id': 'test-session',
                   'hook_event_name': name, **extra}
        return controller.handle(payload, self.home, self.root, self.run, self.clock)

    def arm(self):
        return self.event('UserPromptSubmit', prompt=controller.MARKER + '\nDo the daily work.')

    def test_repeated_early_stops_automatically_continue_until_published(self):
        self.arm()
        self.run.side_effect = [(1, '2/20 complete'), (1, '19/20 complete'),
                                (1, '20/20 but push failed'), (0, '20/20 pushed')]
        for index in range(3):
            result = self.event('Stop', stop_hook_active=index > 0)
            self.assertEqual(result['decision'], 'block')
            self.assertIn(f'continuation {index+1}', result['reason'])
        self.assertNotIn('decision', self.event('Stop', stop_hook_active=True))
        count = self.run.call_count
        self.assertEqual(self.event('Stop'), {})
        self.assertEqual(self.run.call_count, count)

    def test_unrelated_chat_cannot_arm_controller(self):
        self.assertEqual(self.event('UserPromptSubmit', prompt='Fix this project.'), {})
        self.assertEqual(self.event('Stop'), {})
        self.run.assert_not_called()

    def test_user_interrupt_prevents_resumption(self):
        self.arm()
        self.event('Interrupt')
        self.run.reset_mock()
        self.assertEqual(self.event('Stop'), {})
        self.run.assert_not_called()

    def test_paused_automation_prevents_resumption(self):
        self.arm()
        (self.home / 'automation.toml').write_text('status = "PAUSED"\n')
        self.run.reset_mock()
        self.assertEqual(self.event('Stop'), {})
        self.run.assert_not_called()

    def test_date_survives_midnight_and_controller_process_restart(self):
        self.arm()
        self.clock = self.clock.replace(day=28)
        self.run.return_value = (1, 'unfinished')
        self.assertEqual(self.event('Stop')['decision'], 'block')
        self.run.assert_called_with('check', '2026-11-27')

    def test_next_scheduled_run_recovers_unfinished_assignment(self):
        self.arm()
        payload = {'cwd': str(self.root), 'session_id': 'next-session',
                   'hook_event_name': 'UserPromptSubmit',
                   'prompt': controller.MARKER + '\nDaily work.'}
        controller.handle(payload, self.home, self.root, self.run, self.clock.replace(day=28))
        self.run.assert_called_with('plan', '2026-11-27')

    def test_failed_planning_still_arms_stop_controller(self):
        self.run.return_value = (1, 'planning error')
        self.arm()
        self.assertEqual(self.event('Stop')['decision'], 'block')

    def test_desktop_automation_header_still_arms_controller(self):
        self.event('UserPromptSubmit', prompt='Automation: Daily audit\n' + controller.MARKER + '\nDo the work.')
        self.run.return_value = (1, 'not pushed')
        self.assertEqual(self.event('Stop')['decision'], 'block')

    def test_recovery_completion_retires_older_binding(self):
        self.arm()
        payload = {'cwd': str(self.root), 'session_id': 'next-session',
                   'hook_event_name': 'UserPromptSubmit',
                   'prompt': controller.MARKER + '\nDaily work.'}
        controller.handle(payload, self.home, self.root, self.run, self.clock.replace(day=28))
        payload['hook_event_name'] = 'Stop'
        controller.handle(payload, self.home, self.root, self.run, self.clock.replace(day=28))
        old = json.loads((self.home / 'controller-sessions/test-session.json').read_text())
        self.assertEqual(old['status'], 'complete')

    def test_scheduler_tool_output_arms_at_stop_without_user_prompt_event(self):
        transcript = self.root / 'scheduler.jsonl'
        transcript.write_text('\n'.join(json.dumps(x) for x in [
            {'type': 'session_meta', 'payload': {'id': 'test-session', 'cwd': str(self.root), 'thread_source': 'automation'}},
            {'type': 'response_item', 'payload': {'type': 'function_call_output',
             'name': 'automation_update', 'namespace': 'codex_app',
             'output': 'Automation ID: byteseismic-daily-editorial-audit\n' + controller.MARKER}}
        ]) + '\n')
        self.run.side_effect = [(0, 'planned'), (1, 'uncommitted evidence')]
        result = self.event('Stop', transcript_path=str(transcript))
        self.assertEqual(result['decision'], 'block')
        self.assertEqual(self.run.call_count, 2)

    def test_scheduled_interrupt_before_first_stop_is_respected(self):
        transcript = self.root / 'scheduler.jsonl'
        transcript.write_text('\n'.join(json.dumps(x) for x in [
            {'type': 'session_meta', 'payload': {'id': 'test-session', 'cwd': str(self.root), 'thread_source': 'automation'}},
            {'type': 'response_item', 'payload': {'type': 'function_call_output',
             'name': 'automation_update', 'namespace': 'codex_app',
             'output': 'Automation ID: byteseismic-daily-editorial-audit\n' + controller.MARKER}}
        ]) + '\n')
        self.event('Interrupt', transcript_path=str(transcript))
        self.assertEqual(self.event('Stop', transcript_path=str(transcript)), {})
        self.run.assert_not_called()

    def test_arbitrary_transcript_text_cannot_arm(self):
        transcript = self.root / 'other.jsonl'
        transcript.write_text(json.dumps({'type': 'response_item', 'payload': {
            'type': 'message', 'content': controller.MARKER}}) + '\n')
        self.assertEqual(self.event('Stop', transcript_path=str(transcript)), {})
        self.run.assert_not_called()

    def test_additional_review_run_uses_its_own_gate_and_does_not_release_other_run(self):
        self.arm()
        other = {'cwd': str(self.root), 'session_id': 'extra-run',
                 'hook_event_name': 'UserPromptSubmit',
                 'prompt': controller.MARKER + '\n[byteseismic-run:review-recovery]\nReview twenty new pages.'}
        controller.handle(other, self.home, self.root, self.run, self.clock)
        self.run.assert_called_with('plan', '2026-11-27', 'review-recovery')
        other['hook_event_name'] = 'Stop'
        self.run.return_value = (1, '0/20 reviewed')
        self.assertEqual(controller.handle(other, self.home, self.root, self.run, self.clock)['decision'], 'block')
        self.run.assert_called_with('check', '2026-11-27', 'review-recovery')
        self.run.return_value = (0, 'published')
        controller.handle(other, self.home, self.root, self.run, self.clock)
        normal = json.loads((self.home / 'controller-sessions/test-session.json').read_text())
        self.assertEqual(normal['status'], 'active')


if __name__ == '__main__':
    unittest.main()
