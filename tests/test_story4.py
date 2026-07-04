import unittest
from story4.src.modules.core_logic import filter_courses 

class TestStory4(unittest.TestCase):
    def setUp(self):
        self.course_list = ["CS120: Intro", "CS222: Data", "MATH100: Calc"]

    def test_filter_by_cs_prefix(self):
        result = filter_courses(self.course_list, "CS")
        self.assertEqual(len(result), 2)
        self.assertIn("CS120: Intro", result)

    def test_no_match(self):
        result = filter_courses(self.course_list, "PHYS")
        self.assertEqual(result, [])

    def test_empty_course_list(self):
        result = filter_courses([], "CS")
        self.assertEqual(result, [])

    def test_case_insensitive(self):
        result = filter_courses(self.course_list, "cs")
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()