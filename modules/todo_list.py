def start():
    tasks = []

    while True:
        print("\n=========== TO-DO LIST ===========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter Task: ")
            tasks.append(task)
            print("Task Added Successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("No Tasks Found!")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i])

        elif choice == "3":
            if len(tasks) == 0:
                print("No Tasks to Delete!")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i])

                task_number = int(input("Enter task number to delete: "))

                if task_number >= 1 and task_number <= len(tasks):
                    tasks.pop(task_number - 1)
                    print("Task Deleted Successfully!")
                else:
                    print("Invalid Task Number!")

        elif choice == "4":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid Choice!")