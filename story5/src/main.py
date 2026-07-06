from student_input import get_student_input
from schedule_handler import handle_no_schedule

def main(schedule):

    schedule = None  # placeholder for Story 4 output

    while True:

        # TODO: replace with teammate scheduler
        schedule = None

        if schedule is None:

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


if __name__ == "__main__":
    main()
