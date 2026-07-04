from story4.src.modules.data_utils import load_courses_from_file
from story4.src.modules.core_logic import filter_courses

def main():
    courses = load_courses_from_file('data/courses.txt')
    selected = filter_courses(courses, "CS")
    print(f"Selected courses: {selected}")

if __name__ == "__main__":
    main()