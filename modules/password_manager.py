import json
import os

FILE_NAME = "data/passwords.json"


def start():

    print("========== PASSWORD MANAGER ==========")

    while True:

        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Back")

        choice = input("Choose an option: ")

        if choice == "1":

            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            data[website] = {
                "username": username,
                "password": password
            }

            with open(FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)

            print("Password Saved Successfully!")

        elif choice == "2":

            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            if not data:
                print("No passwords found.")
                continue

            for website, details in data.items():
                print(f"\nWebsite : {website}")
                print(f"Username: {details['username']}")
                print(f"Password: {details['password']}")

        elif choice == "3":

            website = input("Enter website: ")

            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            if website in data:
                print(f"\nUsername: {data[website]['username']}")
                print(f"Password: {data[website]['password']}")
            else:
                print("Website not found.")

        elif choice == "4":

            break

        else:

            print("Invalid Choice!")