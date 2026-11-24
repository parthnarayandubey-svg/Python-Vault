import random


def start():
    print("\n========== NUMBER GUESSING GAME ==========")

    secret_number = random.randint(1, 100)

    print("I have selected a number between 1 and 100.")

    guess = int(input("Enter your guess: "))

    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts +=1

        if guess == secret_number:
            print("Correct!")
            print(f"You guessed it in {attempts} attempts.")
            break

        elif guess < secret_number:
            print(" Too Low!")

        else:
            print(" Too High!")