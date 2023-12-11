# To-Do List Application

# Function to display the menu options
def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Save and Quit")

# Function to view tasks from the file
def view_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("\nTasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nNo tasks available.")
    except FileNotFoundError:
        print("\nNo tasks available.")

# Function to add a task to the file
def add_task():
    task = input("\nEnter the task: ")
    with open('tasks.txt', 'a') as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Function to mark a task as complete
def complete_task():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as complete: "))
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = f"[DONE] {tasks[task_number - 1]}"
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Main function to run the To-Do List
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Saving and quitting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
