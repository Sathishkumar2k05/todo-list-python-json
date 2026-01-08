import json
import os
from datetime import datetime

class Task:
    
    def __init__(self, json_file = "task.json"):

        self.jsonfile = json_file

        self.tasks = self.load_task()
    
    def load_task(self):

        if not os.path.exists(self.jsonfile):

            return []
        
        with open(self.jsonfile, "r") as file:

            return json.load(file)
        
    def save_task(self):

        with open(self.jsonfile, "w") as file:

            return json.dump(self.tasks, file, indent = 4)
        
    def get_valid_int(self, message):

        try:

            return int(input(message))
        
        except ValueError:

            print("Invalid input! Try Again!")

            print()

            return None

    
    def add_task(self):

        print(" --- Add Task --- ")

        task_no = self.get_valid_int("Enter task number : ")

        if task_no is None:

            return

        task_name = input("Enter a task : ")

        for task in self.tasks:

            if task['task_number'] == task_no:

                print("Duplicate entry! Task number must be unique")

                print()

                break

        else:

            task = {
                "task_number" : task_no,
                "task_name" : task_name,
                "completed" : False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at":None
            }

            self.tasks.append(task)

            self.save_task()

            print("Task Added Successfully!")

            print()

    def view_task(self):

        print(" --- All Tasks --- ")

        if not self.tasks:

            print("Task not found!")

            print()

        else:

            for task in self.tasks:

                status = "Done" if task.get("completed") else "Pending..."

                print(
                    f"Task Number : {task['task_number']} | "
                    f"Task : {task['task_name']} | "
                    f"Status : {status} | "
                    f"Created : {task['created_at']} | "
                    f"Updated : {task['updated_at']}"
                )


            print()

    def mark_completed(self):

        print(" --- Mark Tasks --- ")

        task_no = self.get_valid_int("Enter task number to mark : ")

        if task_no is None:

            return

        for task in self.tasks:

            if task["task_number"] == task_no:

                task["completed"] = True

                self.save_task()

                print("Task marked as completed!")

                print()

                return()
            
        print("Task not found!")

        print()

    def get_task_by_number(self):

        print(" --- Search Task --- ")

        task_no = self.get_valid_int("Enter task number to search : ")

        if task_no is None:

            return

        found = False

        for task in self.tasks:

            if task["task_number"] == task_no:

                found = True

                status = "Done" if task.get("completed") else "Pending..."

                print(
                    f"Task Number : {task['task_number']} | "
                    f"Task : {task['task_name']} | "
                    f"Status : {status} | "
                    f"Created : {task['created_at']} | "
                    f"Updated : {task['updated_at']}"
                )

                print()

                break

        if not found:

            print("Task not found!")

            print()

    def update_task(self):

        print(" --- Update Task --- ")

        task_no = self.get_valid_int("Enter task number to update : ")

        if task_no is None:

            return

        found = False

        for task in self.tasks:

            if task["task_number"] == task_no:

                task["task_name"] = input("Enter New Task : ")

                print("Select Task Status")
                print("1. Completed")
                print("0. Not completed")

                choice = input("Enter you choice (1/0) : ")

                if choice == "1":

                    task["completed"] = True
                
                elif choice == "0":

                    task["completed"] = False

                task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.save_task()

                found = True

                print("Task Updated Successfully!")

                print()

                break

        if not found:

            print("Task not found")

            print()

    def delete_task(self):

        print(" --- Delete Task --- ")

        task_no = self.get_valid_int("Enter task number to delete : ")

        if task_no is None:

            return

        confirm = input("Are you sure (y/n) : ").lower()

        if confirm == "y":

            found = False

            for task in self.tasks:

                if task["task_number"] == task_no:

                    self.tasks.remove(task)

                    self.save_task()

                    found = True

                    print("Task Deleted Successfully!")

                    print()

                    break

            if not found:

                print("task not found!")

                print()

        else:

            print("Delete cancelled")

def main():

    t1 = Task()

    while True:

        print("Add task enter 1")
        print("View task enter 2")
        print("Mark task enter 3")
        print("Search task enter 4")
        print("Update task enter 5")
        print("Delete task enter 6")
        print("Exit enter 7")
        print()

        choice = input("Enter your choice : ")

        if choice == "1":

            t1.add_task()

        elif choice == "2":

            t1.view_task()

        elif choice == "3":

            t1.mark_completed()

        elif choice == "4":
            t1.get_task_by_number()

        elif choice == "5":

            t1.update_task()

        elif choice == "6":

            t1.delete_task()

        elif choice == "7":

            print("Exiting...")

            break

        else:

            print("Invalid choice!")
            
main()



