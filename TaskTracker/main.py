tasks = []

print("Welcome to TaskTracker!")

while True:
    print("\nOptions: 1. Add  2. List  3. Remove  4. Exit") #dispays menu
    choice = input("Choose: ")

    if choice == '1':
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '2':
        print("\nYour Tasks:")
        for t in tasks:
            print(t)

    elif choice == '3': 
        task_to_remove = input("Enter name of task to remove: ")
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            print("Task removed.")
        else:
            print("Task not found.")

    elif choice == '4':
        break