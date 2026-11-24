import random


def start():
    print("\n========== PASSWORD GENERATOR ==========")

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

    length = int(input("Enter password length: "))

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)