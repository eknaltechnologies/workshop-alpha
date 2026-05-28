import json

tasks = []

print("Welcome to To-Do List App")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        data = json.dumps(tasks)
        print("Saved Data:", data)

        print("Task added")

    elif choice == "2":
        if tasks == []:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "3":
        if tasks == []:
            print("No tasks to update")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

            num = int(input("Enter task number: "))

            if num > 0 and num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1] = new_task

                data = json.dumps(tasks)
                print("Updated Data:", data)

                print("Task updated")
            else:
                print("Invalid task number")

    elif choice == "4":
        if tasks == []:
            print("No tasks to delete")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

            num = int(input("Enter task number: "))

            if num > 0 and num <= len(tasks):
                tasks.pop(num - 1)

                data = json.dumps(tasks)
                print("Updated Data:", data)

                print("Task deleted")
            else:
                print("Invalid task number")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
