def handle_no_schedule(schedule):
    """
    User Story 5:
    Handles the case where no valid schedule can be generated.
    """

    if not schedule:
        print("\nNo valid schedule can be found.")

        while True:
            choice = input("Would you like to try again? (Y/N): ").strip().upper()

            if choice == "Y":
                print("Returning to course selection...")
                return True

            elif choice == "N":
                print("Exiting program...")
                return False

            else:
                print("Invalid input. Please enter Y or N.")

    return True