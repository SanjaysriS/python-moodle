import math

while True:
    try:
        user_input = float(input(""))
        if user_input < 0:
            print("Error: Cannot calculate the square root of a negative number.")
        else:
            square_root = math.sqrt(user_input)
            print(f"The square root of {user_input} is {square_root:.2f}")
        break
    except ValueError:
        print("Error: could not convert string to float")
        break
