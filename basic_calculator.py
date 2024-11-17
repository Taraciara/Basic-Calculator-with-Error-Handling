# basic_calculator.py

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            print("Result:", num1 / num2)
        else:
            print("Invalid operator.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# Run the calculator
calculator()
