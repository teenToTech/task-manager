# Project - Task Manager 

import json 

try: 

    with open("tasks.json","r") as file:
        tasks = json.load(file)

except FileNotFoundError:
    tasks = []


def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(tasks,file)

def add_tasks():

    task_name = input("Enter task name : ")
    priority = input("Enter priority(low/Medium/high) : ")

    task = {
        "task_name" : task_name,
        "priority" : priority,
        "status" : False
    }

    tasks.append(task)
    save_tasks()

    print("Tasks saved successfully\n")

def show_tasks():

    if len(tasks) == 0:
        print("No tasks found\n")

    else:

        print("===== Tasks ======")

        for i, t in enumerate(tasks):

            status = "done" if t['status'] else "Pending"

            print(f"{i + 1}. Task name : {t['task_name']} | Priority : {t['priority']} | Status : {status}\n")

def delete_tasks():

    if len(tasks) == 0:
        print("No tasks to delete\n")

    else:

        show_tasks()

        try:

            index = int(input("Enter the index of task you want to delete : "))

            if 0 <= index and index < len(tasks):
                tasks.pop(index)
                save_tasks()
                print("Index deleted successfully\n")

            else:
                print("Enter a valid index\n")

        except ValueError:
            print("Please enter a valid index number\n")

def mark_done():

    if len(tasks) == 0:
        print("No tasks found to mark as done\n")
    
    else:

        show_tasks()

        try : 
            index = int(input("Enter the index of task you want to mark as done : "))
    
            if 0 <= index and index < len(tasks):
                tasks[index]['status'] = True
                save_tasks()
                print("Marked as done\n")

            else:
                print("Enter a valid index\n")

        except ValueError:
            print("Please enter a valid index number\n")


while True:

    print("====== Task Manager ======")
    print("1. Add tasks")
    print("2. Show tasks")
    print("3. Delete tasks")
    print("4. Mark tasks as done")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        add_tasks()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        delete_tasks()

    elif choice == "4":
        mark_done()

    elif choice == "5":
        print("Exiting.....")
        break 

    else:
        print("Invalid input")




    

