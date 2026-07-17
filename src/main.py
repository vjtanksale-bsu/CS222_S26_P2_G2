from src.scheduler import validate_course_input, load_available_courses
"""
main.py

Entry point for Story 3: Enter Course Selections.

As a student trying to schedule courses for the next semester,
I want to enter n distinct course numbers, so that I can specify
the exact courses I want to take.
"""



COURSE_DATA_FILE = "data/courses.txt"


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


def main():
    available_courses = load_available_courses(COURSE_DATA_FILE)
    n = int(input("How many courses would you like to schedule? "))
    selections = get_user_selections(n, available_courses)
    print(f"\nYou have selected {n} courses: {selections}")


if __name__ == "__main__":
    main()

