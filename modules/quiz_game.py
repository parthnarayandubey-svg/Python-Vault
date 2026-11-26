def start():
    print("\n========== QUIZ GAME ==========\n")

    quiz = [
        {
            "question": "What is the capital of India?",
            "options": [
                "A. Mumbai",
                "B. New Delhi",
                "C. Chennai",
                "D. Kolkata"
            ],
            "answer": "B"
        },
        {
            "question": "Who developed Python?",
            "options": [
                "A. Dennis Ritchie",
                "B. James Gosling",
                "C. Guido van Rossum",
                "D. Elon Musk"
            ],
            "answer": "C"
        },
        {
            "question": "How many continents are there?",
            "options": [
                "A. 5",
                "B. 6",
                "C. 7",
                "D. 8"
            ],
            "answer": "C"
        }
    ]

    score = 0

    for question in quiz:
        print(question["question"])

        for option in question["options"]:
            print(option)

        answer = input("\nEnter your answer (A/B/C/D): ").upper()

        if answer == question["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(" Wrong!")
            print("Correct Answer:", question["answer"])
            print()

    print("==========================")
    print("Quiz Finished!")
    print("Your Score:", score, "/", len(quiz))

    if score == len(quiz):
        print(" Excellent!")
    elif score >= 2:
        print(" Good Job!")
    else:
        print(" Keep Practicing!")

    print("==========================")