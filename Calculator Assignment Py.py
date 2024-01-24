import math  # Import the math module for log and factorial functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero.")
        return None

def factorial(x):
    # Factorial function using math module
    return math.factorial(x)

def x_power_y(x, y):
    return x ** y

def log(x):
    # Logarithm (base 10) using math module
    return math.log10(x)

def ln(x):
    # Natural logarithm using math module
    return math.log(x)

def menu():
    # Display menu options to the user
    print("Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. x^y (Exponentiation)")
    print("7. Log (base 10)")
    print("8. Ln (Natural Log)")
    print("9. Quit")

    # Get user's choice
    choice = input("Enter your choice (1-9): ")
    return choice

def main():
    while True:
        # Get user's choice from the menu
        choice = menu()

        # Check if the user wants to quit
        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Get numeric input from the user
            num1 = float(input("Enter the number: "))

            # For factorial, x_power_y, log, and ln, take a single input
            if choice in ['5', '6', '7', '8']:
                result = None
                if choice == '5':
                    result = factorial(num1)
                elif choice == '6':
                    exponent = float(input("Enter the exponent: "))
                    result = x_power_y(num1, exponent)
                elif choice == '7':
                    result = log(num1)
                elif choice == '8':
                    result = ln(num1)
                print(f"Result: {result}")

            # For basic arithmetic operations, take a second input
            else:
                num2 = float(input("Enter the second number: "))
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                print(f"Result: {result}")

        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter numeric values.")
            continue

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
#LEON NYAZENGA UNICAF UNIVERSITY R1911D9670033