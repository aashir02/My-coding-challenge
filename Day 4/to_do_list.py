tasks = []
choice = 0

while choice != 5:
    print("\n1. Add new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Remove task")
    print("5. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = {}
        task["description"] = input("Enter task description: ")
        task["completed"] = False
        tasks.append(task)

    elif choice == 2:
        if tasks:
            print("Your task list:")
            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['description']} - {status}")
        else:
            print("\nNo tasks yet")

    elif choice == 3:
        if tasks:
            print("Your task list:")
            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['description']} - {status}")

            marked = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= marked < len(tasks):
                tasks[marked]["completed"] = True
                print("Task marked as complete")
            else:
                print("Invalid task number")
        else:
            print("\nNo tasks yet")

    elif choice == 4:
        if tasks:
            print("Your task list:")
            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['description']} - {status}")

            remove = int(input("Enter the task number to remove: ")) - 1
            if 0 <= remove < len(tasks):
                removed_task = tasks.pop(remove)
                print(f"Task '{removed_task['description']}' removed")
            else:
                print("Invalid task number")
        else:
            print("\nNo tasks yet")

    elif choice == 5:
        print("Quitting the program. Goodbye!")
    else:
        print("Invalid choice. Please choose a valid option.")
