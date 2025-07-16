# calculator.py

# -----------------------------
# Command Line Calculator App
# -----------------------------
# Objective:
# Create a command line calculator supporting basic operations
# using Python functions and user input. The program should run
# in a loop until the user chooses to exit.
# -----------------------------

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# Main function for user interaction
def main():
    print("=== Command Line Calculator ===")
    print("Supported Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        # Take operation input from user
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        # Exit condition
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Validate choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option (1-5).")
            continue

        # Take number input from user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        # Perform operation based on user choice
        if choice == '1':
            result = add(num1, num2)
            symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            symbol = '/'

        # Display result
        print(f"Result: {num1} {symbol} {num2} = {result}")

# Run the program
if __name__ == "__main__":
    main()
