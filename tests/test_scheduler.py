import unittest
from src.scheduler import validate_course_input

class TestStory3(unittest.TestCase):
    def setUp(self):
        self.available = ["CS120", "CS121", "CS222"]
        self.selected = []

    def test_invalid_course(self):
        is_valid, msg = validate_course_input(2, "CS999", self.available, self.selected)
        self.assertFalse(is_valid)

    def test_duplicate_course(self):
        self.selected = ["CS120"]
        is_valid, msg = validate_course_input(2, "CS120", self.available, self.selected)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()