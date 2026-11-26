import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import editorial_daily_gate as gate


class DailyGateTests(unittest.TestCase):
    def completed_day_plan(self):
        # A date can contain separately authorized assignments. Exercise the
        # frozen daily plan, never combine every report into a new assignment.
        return gate.read(gate.ROOT, gate.assignment_path('2026-11-26'))

    def test_additional_assignment_cannot_replace_or_create_daily_work(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(ValueError, 'explicitly prepared'):
                gate.assignment(root, '2026-11-26', 'review-recovery')
            with self.assertRaises(ValueError):
                gate.assignment_path('2026-11-26', '../escape')
            self.assertNotEqual(gate.assignment_path('2026-11-26'),
                                gate.assignment_path('2026-11-26', 'review-recovery'))

    def test_real_completed_day_and_missing_evidence(self):
        plan = self.completed_day_plan()
        errors, files = gate.evidence(gate.ROOT, plan)
        self.assertEqual(errors, [])
        self.assertGreater(len(files), 60)
        rows = gate.records(gate.ROOT, plan['date'])
        rows.pop(plan['pagePaths'][-1])
        with patch.object(gate, 'records', return_value=rows):
            errors, _ = gate.evidence(gate.ROOT, plan)
        self.assertTrue(any(plan['pagePaths'][-1] in error for error in errors))

    def test_two_pages_cannot_pass_twenty_page_target(self):
        plan = self.completed_day_plan()
        plan['pagePaths'] = plan['pagePaths'][:2]
        self.assertTrue(gate.evidence(gate.ROOT, plan)[0])

    def test_duplicates_do_not_count(self):
        plan = {'date': '2026-11-26', 'target': 20, 'remainingAtPlanning': 135,
                'pagePaths': ['/same/'] * 20}
        self.assertTrue(gate.evidence(gate.ROOT, plan)[0])

    def test_changed_page_fails(self):
        plan = self.completed_day_plan()
        with patch.object(gate, 'sha', return_value='changed'):
            errors, _ = gate.evidence(gate.ROOT, plan)
        self.assertTrue(any('current page does not match' in error for error in errors))

    def test_missing_build_fails(self):
        original = gate.read
        def read(root, path):
            if 'batch-verification-' in str(path):
                raise FileNotFoundError(path)
            return original(root, path)
        plan = self.completed_day_plan()
        with patch.object(gate, 'read', side_effect=read):
            errors, _ = gate.evidence(gate.ROOT, plan)
        self.assertTrue(any('Missing or invalid full-build record' in error for error in errors))

    def test_unpushed_or_uncommitted_cannot_pass(self):
        def git(root, *args):
            return {'ls-files': 'a', 'diff': 'changed', 'rev-parse': 'local',
                    'ls-remote': 'remote refs/heads/main'}[args[0]]
        with patch.object(gate, 'git', side_effect=git):
            self.assertEqual(len(gate.publication(gate.ROOT, {'a'})), 2)

    def test_plan_resumes_without_selecting_twenty_more(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'quality').mkdir()
            (root / gate.DATA).mkdir()
            queue = [{'pagePath': f'/p{i}/'} for i in range(25)]
            tracker = {'cursor': {'cycle': 8, 'completedPagePathsInCurrentCycle': []}, 'pages': queue}
            file = root / 'quality/editorial-audit-tracker.json'
            file.write_text(json.dumps(tracker))
            plan, _ = gate.assignment(root, '2026-11-27')
            self.assertEqual(plan['target'], 20)
            tracker['cursor']['completedPagePathsInCurrentCycle'] = [x['pagePath'] for x in queue[:2]]
            file.write_text(json.dumps(tracker))
            self.assertEqual(gate.assignment(root, '2026-11-27')[0], plan)
            tracker['cursor']['completedPagePathsInCurrentCycle'] = [x['pagePath'] for x in queue[:22]]
            file.write_text(json.dumps(tracker))
            final, _ = gate.assignment(root, '2026-11-28')
            self.assertEqual(final['target'], 3)
            self.assertTrue(final['endpointException'])


if __name__ == '__main__':
    unittest.main()
