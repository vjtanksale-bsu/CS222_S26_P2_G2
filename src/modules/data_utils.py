def load_courses_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def get_unique_course_numbers(course_lines):
    return list(dict.fromkeys(line.split()[0] for line in course_lines if line.split()))
