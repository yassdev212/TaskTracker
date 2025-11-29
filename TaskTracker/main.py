tasks = []

print ("welcome to tasktracker!")

while True:
    print("\nOptions: 1. Add Task  2. Exit")
    choice = input("Choose: ")

    if choice == '1':
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added.")
    
    elif choice == '2':
        break