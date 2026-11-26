def start():

    expenses = []

    while True:
        print("\n=========== EXPENSE TRACKER ===========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Expense Name: ")
            amount = float(input("Enter Amount: "))

            expense = [name, amount]
            expenses.append(expense)

            print("Expense Added Successfully!")

        elif choice == "2":
            if len(expenses) == 0:
                print("No Expenses Found!")

            else:
                print("\nYour Expenses:")

                for i in range(len(expenses)):
                    print(i + 1, ".", expenses[i][0], "- ₹", expenses[i][1])

        elif choice == "3":
            total = 0

            for i in range(len(expenses)):
                total = total + expenses[i][1]

            print("\nTotal Expense = ₹", total)

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid Choice!")