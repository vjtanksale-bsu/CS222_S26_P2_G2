"""
scheduler.py

Story 3: Enter Course Selections.

Provides:
    - load_available_courses: reads offered course numbers from a
      course data file.
    - validate_course_input: validates a single course number a
      student enters while building their course selection list.
"""

import os


def load_available_courses(filepath):
    """
    Reads a course data file and returns the sorted list of unique
    course numbers offered.

    Each line of the file is expected to be whitespace/tab separated:
        <course_number> <section> <days> <start_time> <end_time>
    Only the first column (course_number) is used here; a single
    course number may appear on multiple lines (one per section).

    Args:
        filepath (str): path to the course data file.

    Returns:
        list[str]: sorted list of unique, uppercase course numbers.

    Raises:
        FileNotFoundError: if filepath does not exist.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Course data file not found: {filepath}")

    course_numbers = set()
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            course_number = line.split()[0]
            course_numbers.add(course_number.upper())

    return sorted(course_numbers)


def validate_course_input(n, user_input, available_courses, selected_list):
    """
    Validates a single course number entered by the user.

    Validation logic (Story 3 acceptance criteria):
        1. Reject empty/whitespace-only input.
        2. Reject a course number that is not offered.
        3. Reject a course number already selected (duplicate).

    Args:
        n (int): total number of courses the user needs to select.
            Reserved for callers that want to report progress; not
            used directly in validation since the caller controls
            how many times this function is invoked.
        user_input (str): the raw course number entered by the user.
        available_courses (list[str]): all course numbers offered.
        selected_list (list[str]): course numbers already selected.

    Returns:
        tuple[bool, str]: (is_valid, message). message is "Success"
        when is_valid is True, otherwise a user-facing error message.
    """
    course = user_input.strip().upper()

    if not course:
        return False, "Error: Course number cannot be empty. Please try again."

    if course not in available_courses:
        return False, f"Error: Course {course} does not exist. Please try again."

    if course in selected_list:
        return False, (
            f"Error: Course {course} has already been selected. "
            "You cannot select it twice."
        )

    return True, "Success"

def sections_conflict(section1, section2):

    days1 = section1[2]
    days2 = section2[2]

    start1 = int(section1[3])
    end1 = int(section1[4])

    start2 = int(section2[3])
    end2 = int(section2[4])

    if not any(day in days2 for day in days1):
        return False
    return start1 < end2 and start2 < end1


def generate_schedule(selected, raw):
 
    course_sections = {}
    for course in selected:
        sections = []
        for line in raw:
            parts = line.split()
            if parts[0] == course:
                sections.append(parts)
        course_sections[course] = sections

    def backtrack(index, schedule):
        if index == len(selected):
            return list(schedule)

        course = selected[index]
        for section in course_sections[course]:
            if all(not sections_conflict(section, existing) for existing in schedule):
                schedule.append(section)
                result = backtrack(index + 1, schedule)
                if result is not None:
                    return result
                schedule.pop()

        return None

    result = backtrack(0, [])
    if result is None:
        return []
    return [" ".join(section) for section in result]