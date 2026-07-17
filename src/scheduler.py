def validate_course_input(n, user_input, available_courses, selected_list):
    """
    Validation logic:
    1. Check if the course exists
    2. Check for duplicates
    Returns (is_valid, error_message)
    """
    if user_input not in available_courses:
        return False, f"Error: Course {user_input} does not exist. Please try again."
    if user_input in selected_list:
        return False, f"Error: Course {user_input} has already been selected. You cannot select it twice."
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