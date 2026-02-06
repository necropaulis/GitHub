tasks = []

def show_menu(): #  Options to be Displayed
    print("\n1. Add A Task")
    print("2. View Tasks")
    print("3. Remove A Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ") # Shows Options

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task) # .append is used to change the list
        print(f"Task '{task}' added.") # f formats list to input

    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("\nNo tasks available.")

    elif choice == "3":
        if tasks:
            try:
                index = int(input("Enter the number of the task to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to remove.")

    elif choice == "4":
        print("Exiting the To-Do List application.")
        break

    else:
        print("Invalid choice. Please try again.")