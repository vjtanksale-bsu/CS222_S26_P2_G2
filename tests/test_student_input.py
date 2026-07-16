import pytest
from unittest.mock import patch
from src.student_input import get_student_input

class TestStudent:
    def test_valid_input_returns_integer(self):
        with patch('builtins.input', return_value='5'):
            result = get_student_input()
            assert isinstance(result, int)
            assert result == 5
    def test_invalid_input_zero(self):
        with patch('builtins.input', side_effect=['0', '5']):
            result = get_student_input()
            assert result == 5
    def test_invalid_input_negative(self):
        with patch('builtins.input', side_effect=['-3', '5']):
            result = get_student_input()
            assert result == 5
    def test_invalid_input_non_integer(self):
        with patch('builtins.input', side_effect=['abc', '5']):
            result = get_student_input()
            assert result == 5
    def test_invalid_input_float(self):
        with patch('builtins.input', side_effect=['3.14', '5']):
            result = get_student_input()
            assert result == 5
    def test_input_cannot_exceed_available_courses(self):
        with patch('builtins.input', side_effect=['10', '3']):
            result = get_student_input(max_courses=5)
            assert result == 3
