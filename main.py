from modules import calculator
from modules import password_generator
from modules import guessing_game
from modules import quiz_game
from modules import todo_list


print("==========================")
print("        PYTHON VAULT")
print("==========================")
print("Welcome, Parth!")
print()
print("1. calculator ")
print("2. Password Generator")
print("3. Number Guessing Game")
print("4. Quiz Game")
print("5. To-Do list")
print("6. Exit")
print()
choice = input("Choose an option: ")

if choice == "1":
    print("Opening Calculator...")
    calculator.start()

elif choice == "2":
    password_generator.start()

elif choice == "3":
    guessing_game.start()

elif choice == "4":
    quiz_game.start()

elif choice == "5":
    todo_list.start()

elif choice == "6":
    print("Goodbye!!")

else:
    print("invalid!!")