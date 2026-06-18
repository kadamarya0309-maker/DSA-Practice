def main():
    while True:
        print("~"*10)
        print("To Do List")
        print("1.Add task")
        print("2.Delete Task")
        print("3.Mark Task as complete")
        print("4.View Task")
        print("5.Exit")

        choice=int(input("Enter the operation to perform:"))

        if choice==1:
            add_task()
        elif choice==2:
            delete_task()
        elif choice==3:
            mark_task()
        elif choice==4:
            view_task()
        elif choice==5:
            exit()
        else:
            print("Invalid choice")

tasks=[]

def add_task():
    task=input("Enter Your task:")
    if len(task)==0:
        print("Please enter the task")
    else:
        tasks.append(task)
        print("Task Added..!!!!")

def view_task():
    for i,task in enumerate(tasks):
        print(f"{i+1}.{task}")

def delete_task():
    view_task()
    delete=int(input("Enter the task no to delete:"))
    if delete==0 or delete>len(tasks):
        print("Please Enter the valid number")
    else:
        tasks.pop(delete-1)

def mark_task():
    view_task()
    mark=int(input("Enter the task to mark as COMPLETED:"))
    if mark==0 or mark>len(tasks):
        print("Please Enter the valid number")
    else:
        for i,task in enumerate(tasks):
            if i==mark:
                print(f"{i}.{task} DONE..!!!!")

if __name__ == "__main__":
    main()