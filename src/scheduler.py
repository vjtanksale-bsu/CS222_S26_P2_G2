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