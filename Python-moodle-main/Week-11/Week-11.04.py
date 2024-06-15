while True:
    try:
        num1 = int(input(""))
        num2 = int(input(""))
        
        division_result = num1 / num2
        modulo_result = num1 % num2
        
        print(f"Division result: {division_result}")
        print(f"Modulo result: {modulo_result}")
        break
    
    except ValueError:
        print("Error: Non-numeric input provided.")
        break
    
    except ZeroDivisionError:
        print("Error: Cannot divide or modulo by zero.")
        break
