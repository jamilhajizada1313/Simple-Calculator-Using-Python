
print("================================")
print("       PYTHON CALCULATOR")
print("================================")

while True:

    # Get numbers from the user
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    # Display operation menu
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user's choice
    choice = int(input("\nEnter your choice: "))

    # Check the selected operation
    if choice == 1:
        result = num1 + num2
        print("\nResult:", num1, "+", num2, "=", result)

    elif choice == 2:
        result = num1 - num2
        print("\nResult:", num1, "-", num2, "=", result)

    elif choice == 3:
        result = num1 * num2
        print("\nResult:", num1, "*", num2, "=", result)

    elif choice == 4:

        if num2 == 0:
            print("\nError: Division by zero is not allowed.")

        else:
            result = num1 / num2
            print("\nResult:", num1, "/", num2, "=", result)

    else:
        print("\nError: Invalid operation!")

    # Ask user whether to continue
    again = input("\nWould you like to perform another calculation? (yes/no): ")

    if again.lower() == "no":
        print("\nThank you for using the calculator!")
        break
