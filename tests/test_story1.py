from src.modules.data_utils import get_unique_course_numbers


def test_unique_course_numbers_removes_duplicates():
    raw_courses = [
        "CS222 001 MWF 0900 0950",
        "CS222 002 TR 1100 1215",
        "MATH165 001 MWF 1000 1050",
    ]

    result = get_unique_course_numbers(raw_courses)

    assert result == ["CS222", "MATH165"]


def test_unique_course_numbers_ignores_blank_lines():
    raw_courses = [
        "",
        "   ",
        "CS120 001 MWF 0800 0850",
    ]

    result = get_unique_course_numbers(raw_courses)

    assert result == ["CS120"]
