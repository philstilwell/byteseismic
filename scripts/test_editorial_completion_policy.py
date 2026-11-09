"""Exercise the endpoint without changing the saved editorial queue."""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch
import editorial_audit_tracker as audit


class CompletionPolicyTests(unittest.TestCase):
    def setUp(self):
        self.tracker = json.loads((Path(__file__).resolve().parents[1] / 'quality/editorial-audit-tracker.json').read_text())
        self.tracker['protocol']['stopAfterCurrentCycle'] = True
        self.pages = self.tracker['pages']
        self.cycle = self.tracker['cursor']['cycle']

    def near_end(self, remaining=10):
        tracker = copy.deepcopy(self.tracker)
        done = [p['pagePath'] for p in self.pages[:-remaining]]
        tracker['cursor']['completedPagePathsInCurrentCycle'] = done
        tracker['currentBatch'] = audit._batch_from_remaining(self.pages, set(done), 50, self.cycle)
        return tracker

    def test_final_batch_stops_and_repeat_is_noop(self):
        tracker = self.near_end()
        expected = [p['pagePath'] for p in tracker['currentBatch']['pages']]
        result = audit.advance_editorial_audit_tracker(tracker)
        self.assertEqual(result['cursor']['cycle'], self.cycle)
        self.assertEqual(result['cursor']['lastCompletedBatch']['pagePaths'], expected)
        self.assertEqual(len(result['cursor']['completedPagePathsInCurrentCycle']), len(self.pages))
        self.assertEqual(result['summary']['pagesRemainingInCurrentCycle'], 0)
        self.assertEqual(result['currentBatch']['pages'], [])
        self.assertEqual(result['upcomingBatches'], [])
        self.assertEqual(result['cursor']['nextPagePath'], '')
        self.assertFalse(result['cursor']['lastCompletedBatch']['wrappedToNextCycle'])
        self.assertEqual(audit.advance_editorial_audit_tracker(copy.deepcopy(result)), result)

    def test_rebuild_preserves_completion_and_policy(self):
        result = audit.advance_editorial_audit_tracker(self.near_end())
        with patch.object(audit, '_aggregate_page_records', return_value=self.pages):
            rebuilt = audit.build_editorial_audit_tracker({}, existing_tracker=result)
        self.assertTrue(rebuilt['protocol']['stopAfterCurrentCycle'])
        self.assertEqual(rebuilt['cursor'], result['cursor'])
        self.assertEqual(rebuilt['currentBatch']['pages'], [])
        self.assertEqual(rebuilt['upcomingBatches'], [])
        self.assertIn('Current pass complete', audit.render_editorial_audit_tracker_markdown(rebuilt))

    def test_unfinished_pass_continues_without_new_cycle_preview(self):
        result = audit.advance_editorial_audit_tracker(self.near_end(60))
        self.assertEqual(result['summary']['pagesRemainingInCurrentCycle'], 10)
        self.assertEqual(result['currentBatch']['pageCount'], 10)
        self.assertEqual(result['upcomingBatches'], [])
        self.assertFalse(result['currentBatch']['wrapsToNextCycle'])

    def test_restart_requires_separate_authorization(self):
        with self.assertRaisesRegex(ValueError, 'separate authorization'):
            audit.restart_editorial_audit_tracker(self.tracker)

    def test_legacy_recurring_mode_still_wraps(self):
        tracker = self.near_end()
        tracker['protocol'].pop('stopAfterCurrentCycle')
        result = audit.advance_editorial_audit_tracker(tracker)
        self.assertEqual(result['cursor']['cycle'], self.cycle + 1)
        self.assertEqual(result['cursor']['completedPagePathsInCurrentCycle'], [])
        self.assertTrue(result['currentBatch']['pages'])


if __name__ == '__main__':
    unittest.main()
