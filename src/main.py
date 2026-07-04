from src.scheduler import validate_course_input

def get_user_selections(n, available_courses):
    selected_courses = []
    print(f"Please enter {n} different course codes in sequence: ")
    
    while len(selected_courses) < n:
        user_input = input(f"Enter course #{len(selected_courses) + 1}: ").strip()
        
        is_valid, message = validate_course_input(n, user_input, available_courses)
        
        if is_valid:
            selected_courses.append(user_input)
            print(f"Added successfully! Currently selected: {selected_courses}")
        else:
            print(message)
            
    return selected_courses
