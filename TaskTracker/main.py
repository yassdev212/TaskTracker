tasks = []

print("Welcome to TaskTracker!")

while True:
    print("\nOptions: 1. Add Task  2. List Tasks  3. Exit") 
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
        break