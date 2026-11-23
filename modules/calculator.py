print("WELCOME TO CALCULATOR!")

print("Calculator Module Loaded!")


import math


def start():
    while True:
        print("\n========== CALCULATOR ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Floor Division")
        print("8. Back")

        choice = input("\nChoose an option: ")

        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result =", num1 + num2)

        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result =", num1 - num2)

        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result =", num1 * num2)

        elif choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print("Result =", num1 / num2)

        elif choice == "5":
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter power: "))
            print("Result =", num1 ** num2)

        elif choice == "6":
            num = float(input("Enter number: "))

            if num < 0:
                print("Square root of negative number is not possible.")
            else:
                print("Result =", math.sqrt(num))

        elif choice == "7":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print("Result =", num1 // num2)

        elif choice == "8":
            break

        else:
            print("Invalid Choice!")