"""
main.py

Entry point for the course scheduler.

Combines Story 3 (enter n distinct, valid course selections) with
the full scheduling flow: loading offered courses, collecting the
student's number of courses, validating each selection, building
the resulting schedule, and handling the case where no schedule
can be found.
"""

import os

from src.scheduler import validate_course_input, generate_schedule
from src.schedule_handler import handle_no_schedule
from src.student_input import get_student_input
from src.modules.data_utils import get_unique_course_numbers, load_courses_from_file


def get_user_selections(n, available_courses):
    """
    Prompts the user to enter n distinct, valid course numbers.

    Keeps prompting until exactly n valid, distinct courses have
    been entered. On invalid input (duplicate or non-existent
    course, or empty input), prints an error message and re-prompts
    without counting the failed attempt, per Story 3's acceptance
    criteria.

    Args:
        n (int): number of distinct courses to collect.
        available_courses (list[str]): all course numbers offered.

    Returns:
        list[str]: the n distinct, validated course numbers.
    """
    selected_courses = []
    print(f"Please enter {n} different course codes in sequence: ")

    while len(selected_courses) < n:
        user_input = input(f"Enter course #{len(selected_courses) + 1}: ")

        is_valid, message = validate_course_input(
            n, user_input, available_courses, selected_courses
        )

        if is_valid:
            selected_courses.append(user_input.strip().upper())
            print(f"Added successfully! Currently selected: {selected_courses}")
        else:
            print(message)

    return selected_courses


def main(schedule=None):
    base = os.path.join(os.path.dirname(__file__), "..", "data")
    raw = (
        load_courses_from_file(os.path.join(base, "courses.txt"))
        + load_courses_from_file(os.path.join(base, "courses1.txt"))
        + load_courses_from_file(os.path.join(base, "courses2.txt"))
    )
    available = get_unique_course_numbers(raw)

    while True:
        selected = []

        print("Available courses:")
        for index, course in enumerate(available, start=1):
            print(f"{index}. {course}")

        n = get_student_input(len(available))
        selected = get_user_selections(n, available)

        schedule = []
        for c in selected:
            for line in raw:
                if line.startswith(c):
                    schedule.append(line)
                    break

        if not schedule:
            retry = handle_no_schedule(schedule)
            if retry:
                print("Restarting course selection...\n")
                continue
            else:
                print("Program ended.")
                return

        print("Valid schedule found:")
        for course in schedule:
            print(course)
        break


if __name__ == "__main__":
    main()
