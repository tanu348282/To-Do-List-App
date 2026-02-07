def task():
    tasks = []  # empty list
    print("------ WELCOME TO TO DO LIST APP ----------")

    total_tasks = int(input("Enter the number of tasks you want to add = "))

    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"\nToday's tasks are: {tasks}")

    while True:
        print("\nChoose an option:")
        print("1 - Add")
        print("2 - Update")
        print("3 - Delete")
        print("4 - View")
        print("5 - Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print("Task added successfully.")

        elif option == 2:
            Updated_task = input("Enter the task name you want to update: ")
            if Updated_task in tasks:
                new_task = input("Enter new task name: ")
                index = tasks.index(Updated_task)
                tasks[index] = new_task
                print("Task updated successfully.")

        elif option == 3:
            delete_task = input("Enter the task name you want to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)
                print("Task deleted successfully.")

        elif option == 4:
            print("Your tasks are:", tasks)

        elif option == 5:
            print("Closing the program. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

task()
