import unittest
import os
import tempfile

from src.scheduler import validate_course_input, load_available_courses


class TestValidateCourseInput(unittest.TestCase):
    """
    Story 3: Enter Course Selections
    
    """

    def setUp(self):
        self.available = ["CS120", "CS121", "CS222"]
        self.selected = []

    def test_valid_course_returns_true(self):
        is_valid, msg = validate_course_input(2, "CS120", self.available, self.selected)
        self.assertTrue(is_valid)
        self.assertEqual(msg, "Success")

    def test_invalid_course_returns_false(self):
        is_valid, msg = validate_course_input(2, "CS999", self.available, self.selected)
        self.assertFalse(is_valid)
        self.assertIn("does not exist", msg)

    def test_duplicate_course_returns_false(self):
        self.selected = ["CS120"]
        is_valid, msg = validate_course_input(2, "CS120", self.available, self.selected)
        self.assertFalse(is_valid)
        self.assertIn("already been selected", msg)

    def test_empty_input_returns_false(self):
        is_valid, msg = validate_course_input(2, "", self.available, self.selected)
        self.assertFalse(is_valid)
        self.assertIn("cannot be empty", msg)

    def test_whitespace_only_input_returns_false(self):
        is_valid, msg = validate_course_input(2, "   ", self.available, self.selected)
        self.assertFalse(is_valid)
        self.assertIn("cannot be empty", msg)

    def test_input_is_case_insensitive(self):
        is_valid, msg = validate_course_input(2, "cs120", self.available, self.selected)
        self.assertTrue(is_valid)

    def test_input_with_surrounding_whitespace_is_trimmed(self):
        is_valid, msg = validate_course_input(2, "  CS120  ", self.available, self.selected)
        self.assertTrue(is_valid)

    def test_duplicate_check_is_case_insensitive(self):
        self.selected = ["CS120"]
        is_valid, msg = validate_course_input(2, "cs120", self.available, self.selected)
        self.assertFalse(is_valid)
        self.assertIn("already been selected", msg)


class TestLoadAvailableCourses(unittest.TestCase):
    """
    Loads the list of offered course numbers from a course data file,
    so validation can check real offerings rather than a hardcoded list.
    """

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".txt"
        )
        self.temp_file.write(
            "MATH166\t007\tMWF\t1100\t1345\n"
            "CS222\t574\tTR\t1500\t1650\n"
            "CS222\t996\tMWF\t1530\t1815\n"
            "CS120\t292\tMWF\t1800\t1850\n"
            "\n"
        )
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_returns_unique_sorted_course_numbers(self):
        result = load_available_courses(self.temp_file.name)
        self.assertEqual(result, ["CS120", "CS222", "MATH166"])

    def test_raises_error_for_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_available_courses("data/does_not_exist.txt")

    def test_ignores_blank_lines(self):
        result = load_available_courses(self.temp_file.name)
        self.assertNotIn("", result)


if __name__ == "__main__":
    unittest.main()
