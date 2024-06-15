def get_input_within_range(min_value, max_value):
    while True:
        try:
            user_input = int(input("Enter a number: "))
            if min_value <= user_input <= max_value:
                print("Valid input.")
                break
            else:
                print("Error: Number out of allowed range.")
        except ValueError:
            print("Error: Invalid literal for int(). Please enter a valid number.")

# Define the range
min_range = 1
max_range = 100

# Call the function with the defined range
get_input_within_range(min_range, max_range)
