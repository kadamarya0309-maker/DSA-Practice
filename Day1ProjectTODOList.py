tasks = []

def add_task():
    task = input("Enter task: ")
    if len(task) == 0:
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added.")

def view_task():
    if len(tasks) == 0:
        print("No tasks found.")
        return
    
    print("\n----------------------------")
    print("  # | Task")
    print("----------------------------")
    
    for i in range(len(tasks)):
        task = tasks[i]
        if task.endswith("[DONE]"):
            display_task = task.replace(" [DONE]", "")
            print(f"{i+1}|{display_task} [DONE]")
        else:
            print(f"{i+1}|{task}")
    
    print("----------------------------")
    print("Total:", len(tasks), "tasks")

def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return
    
    view_task()
    
    print("")
    num = input("Enter task number to delete: ")
    
    if num.isdigit() == False:
        print("Please enter a number.")
        return
    
    num = int(num)
    
    if num < 1 or num > len(tasks):
        print("Invalid number.")
    else:
        removed = tasks.pop(num - 1)
        print("Deleted:", removed)

def mark_task():
    if len(tasks) == 0:
        print("No tasks to mark.")
        return
    
    view_task()
    
    print("")
    num = input("Enter task number to mark as done: ")
    
    if num.isdigit() == False:
        print("Please enter a number.")
        return
    
    num = int(num)
    
    if num < 1 or num > len(tasks):
        print("Invalid number.")
    else:
        task = tasks[num - 1]
        if task.endswith("[DONE]"):
            print("Task already marked as done.")
        else:
            tasks[num - 1] = task + " [DONE]"
            print("Task marked as done.")

def main():
    while True:
        print("\n--------------------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        print("--------------------")
        
        choice = input("Choose (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()