import unittest
from unittest.mock import patch

from src.main import get_user_selections


class TestGetUserSelections(unittest.TestCase):
    """
    Story 3: verifies that exactly n distinct, valid courses are
    collected, and that invalid/duplicate entries cause a re-prompt
    instead of crashing or being accepted.
    """

    def setUp(self):
        self.available = ["CS120", "CS121", "CS222"]

    def test_collects_exactly_n_distinct_courses(self):
        with patch("builtins.input", side_effect=["CS120", "CS121"]):
            result = get_user_selections(2, self.available)
        self.assertEqual(result, ["CS120", "CS121"])
        self.assertEqual(len(result), 2)

    def test_reprompts_on_duplicate_course(self):
        with patch("builtins.input", side_effect=["CS120", "CS120", "CS121"]):
            result = get_user_selections(2, self.available)
        self.assertEqual(result, ["CS120", "CS121"])

    def test_reprompts_on_invalid_course(self):
        with patch("builtins.input", side_effect=["CS999", "CS120", "CS121"]):
            result = get_user_selections(2, self.available)
        self.assertEqual(result, ["CS120", "CS121"])

    def test_reprompts_on_empty_input(self):
        with patch("builtins.input", side_effect=["", "CS120", "CS121"]):
            result = get_user_selections(2, self.available)
        self.assertEqual(result, ["CS120", "CS121"])


if __name__ == "__main__":
    unittest.main()