#Add Task, View Task, Remove Task, Mark Task, Exit


todo_list = []

def show_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice(1-5):")

    if choice == '1':
        task = input("Enter the task to add:")
        todo_list.append(task)
        print(f"Task '{task}' added to the list.")
    elif choice == '2':
        if todo_list:
            print("To-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list.")
    elif choice == '3':
        if todo_list:
            task_num = int(input("Enter the task number to remove:"))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks in the list.")
    elif choice == '4':
        if todo_list:
            task_num = int(input("Enter the task number to mark as completed:"))
            if 1 <= task_num <= len(todo_list):
                completed_task = todo_list[task_num - 1]
                print(f"Task '{completed_task}' marked as completed.")
                todo_list[task_num - 1] = f"{completed_task} (Completed)"
            else:
                print("Invalid task number.")
        else:
            print("No tasks in the list.")
    elif choice == '5':
        print("exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")