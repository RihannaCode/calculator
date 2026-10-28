#===============Built Calculator===================

while True:
    try:
        first_num = float(input("Enter your first number: "))
        second_num = float(input("Enter your second number: "))
        operator = input("Enter operator (+, -, *, /): ")
        

    except ValueError:
        print("Invalid input, Please enter a number.")
        continue

    if operator == "+":
        print(f"Plus: {first_num + second_num}")

    elif operator == "-":
        print(f"Minus: {first_num - second_num}")

    elif operator == "*":
        print(f"Multiply: {first_num * second_num}")

    elif operator == "/":
        if second_num == 0:
            print("Cannot divide by zero")
        else:
            print(f"Divide: {first_num / second_num}")

    else:
        print("Invalid operator")

    choice = input("Press Enter to continue or q to quit: ")

    if choice.lower() == "q":
        print("Goodbye!😎")
        break