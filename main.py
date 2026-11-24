from modules import calculator
from modules import password_generator


print("==========================")
print("        PYTHON VAULT")
print("==========================")
print("Welcome, Parth!")
print()
print("1. calculator ")
print("2. Password Generator")
print("3. Number Guessing Game")
print("4. Quiz Game")
print("5. Exit")
print()
choice = input("Choose an option: ")

if choice == "1":
    print("Opening Calculator...")
    calculator.start()

elif choice == "2":
    password_generator.start()

elif choice == "3":
    print("coming soon..")

elif choice == "4":
    print("Coming Soon..")

elif choice == "5":
    print("Goodbye!!")

else:
    print("invalid!!")