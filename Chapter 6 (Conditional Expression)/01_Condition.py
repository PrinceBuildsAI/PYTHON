def check_even_odd():
    while True:
        try:
            # Get user input
            num = int(input("Enter a number: "))
            
            # Check if the number is even or odd
            if num % 2 == 0:
                print(f"{num} is even.")
            else:
                print(f"{num} is odd.")
            
            # Ask user if they want to check another number
            continue_choice = input("Do you want to check another number? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                print("Exiting the program.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Run the even/odd check function
check_even_odd()
