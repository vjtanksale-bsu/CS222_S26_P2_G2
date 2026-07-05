def get_student_input():
    while True:
        user_input = input("Please enter a positive integer: ")
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Input must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")