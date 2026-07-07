import os
from schedule_handler import handle_no_schedule
from scheduler import validate_course_input
from student_input import get_student_input
from modules.data_utils import load_courses_from_file

def main(schedule=None):
    base = os.path.join(os.path.dirname(__file__), "..", "data")
    raw = (
        load_courses_from_file(os.path.join(base, "courses.txt")) +
        load_courses_from_file(os.path.join(base, "courses1.txt")) +
        load_courses_from_file(os.path.join(base, "courses2.txt"))
    )

    # 提取所有不重复的课程号
    available = list(dict.fromkeys(line.split()[0] for line in raw if line.split()))

    while True:
        schedule = None
        selected = []

        print("Available courses:", ", ".join(available))
        n = get_student_input()

        for i in range(n):
            while True:
                user_input = input(f"Enter course {i+1}: ").strip().upper()
                is_valid, msg = validate_course_input(n, user_input, available, selected)
                if is_valid:
                    selected.append(user_input)
                    break
                print(msg)

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
