import unittest
from unittest.mock import patch
from src.schedule_handler import handle_no_schedule

class TestScheduleHandler(unittest.TestCase):

    @patch('builtins.input', side_effect=["maybe", "Y"])
    def test_retry_yes(self, mock_input):
        result = handle_no_schedule()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=["N"])
    def test_exit(self, mock_input):
        result = handle_no_schedule()
        self.assertFalse(result)