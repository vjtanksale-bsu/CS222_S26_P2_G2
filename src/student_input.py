def get_student_input(max_courses=None):
    while True:
        user_input = input("How many courses would you like to register for? Enter a positive integer: ")
        try:
            value = int(user_input)
            if value <= 0:
                print("Input must be a positive integer. Please try again.")
            elif max_courses is not None and value > max_courses:
                print(f"You can only register for up to {max_courses} available courses. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
