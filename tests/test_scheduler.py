import unittest

from src.scheduler import validate_course_input, sections_conflict, generate_schedule


class TestValidateCourseInput(unittest.TestCase):
    def setUp(self):
        self.available = ["CS120", "CS121", "CS222"]
        self.selected = []

    def test_valid_course_returns_true(self):
        is_valid, msg = validate_course_input(2, "CS120", self.available, self.selected)
        self.assertTrue(is_valid)

    def test_invalid_course_returns_false(self):
        is_valid, msg = validate_course_input(2, "CS999", self.available, self.selected)
        self.assertFalse(is_valid)
        self.assertIn("does not exist", msg)

    def test_duplicate_course_returns_false(self):
        self.selected = ["CS120"]
        is_valid, msg = validate_course_input(2, "CS120", self.available, self.selected)
        self.assertFalse(is_valid)
        self.assertIn("already been selected", msg)


class TestSectionsConflict(unittest.TestCase):
    # section format: [course, section_num, days, start, end]

    def test_no_conflict_different_days(self):
        a = ["CS120", "001", "MWF", "900", "1000"]
        b = ["CS121", "001", "TR", "900", "1000"]
        self.assertFalse(sections_conflict(a, b))

    def test_conflict_same_day_overlapping_time(self):
        a = ["CS120", "001", "MWF", "900", "1100"]
        b = ["CS121", "001", "MW", "1000", "1200"]
        self.assertTrue(sections_conflict(a, b))

    def test_no_conflict_back_to_back(self):
        a = ["CS120", "001", "MWF", "800", "900"]
        b = ["CS121", "001", "M", "900", "1000"]
        self.assertFalse(sections_conflict(a, b))

    def test_no_conflict_no_shared_days_even_if_times_overlap(self):
        a = ["CS120", "001", "T", "900", "1000"]
        b = ["CS121", "001", "R", "900", "1000"]
        self.assertFalse(sections_conflict(a, b))


class TestGenerateSchedule(unittest.TestCase):
    def test_finds_schedule_simple_case(self):
        raw = [
            "CS120 001 MWF 900 1000",
            "CS121 001 TR 900 1000",
        ]
        result = generate_schedule(["CS120", "CS121"], raw)
        self.assertEqual(len(result), 2)

    def test_returns_empty_when_course_not_offered(self):
        raw = ["CS120 001 MWF 900 1000"]
        result = generate_schedule(["CS999"], raw)
        self.assertEqual(result, [])

    def test_returns_empty_when_only_option_conflicts(self):
        raw = [
            "CS120 001 MWF 900 1000",
            "CS121 001 MWF 900 1000",
        ]
        result = generate_schedule(["CS120", "CS121"], raw)
        self.assertEqual(result, [])

    def test_finds_valid_schedule_that_requires_backtracking(self):
        """
        This is the critical case. A valid conflict-free combination
        DOES exist (CS120's 2nd section + CS121's only section), but
        it requires *not* picking CS120's first section. A greedy,
        non-backtracking algorithm that commits to the first
        non-conflicting section it finds for each course, in order,
        will pick CS120-001 (no conflict yet, since nothing is
        scheduled), which then blocks CS121's only section — even
        though swapping to CS120-002 would have made a full valid
        schedule possible.
        """
        raw = [
            "CS120 001 MWF 900 1000",   # picked first by a greedy algorithm
            "CS120 002 TR 900 1000",    # the section actually needed
            "CS121 001 MWF 900 1000",   # CS121's only section
        ]
        result = generate_schedule(["CS120", "CS121"], raw)
        self.assertEqual(
            len(result), 2,
            "A valid conflict-free schedule exists (CS120-002 + CS121-001) "
            "but generate_schedule failed to find it. This means the "
            "algorithm doesn't backtrack when an earlier greedy choice "
            "blocks a later course."
        )


if __name__ == "__main__":
    unittest.main()