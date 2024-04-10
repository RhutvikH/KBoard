import time

class Task:
    def __init__(self, id, title, priority, description, status, assignee, reporter, time_started=time.time()):
        self.id = id
        self.title = title
        self.priority = priority
        self.description = description
        self.status = status
        self.assignee = assignee
        self.reporter = reporter
        self.time_finished = None if status!="Done" else time.time()
        self.time_started = time_started
        self.time_taken = None if status!="Done" else self.time_finished - self.time_started

    def change_title(self, new_title):
        self.title = new_title
    
    def change_description(self, new_description):
        self.description = new_description

    def change_priority(self, new_priority):
        self.priority = new_priority

    def change_status(self, new_status):
        self.status = new_status
        if new_status == "Done":
            self.time_finished = time.time()
            self.time_taken = self.time_finished - self.time_started
    
class KBoard:
    def __init__(self, id, Project_name, created_by):
        self.id = id
        self.Project_name = Project_name
        self.created_by = created_by
        self.used_task_ids=set()
        self.tasks = []
    def add_new_task(self, id, title, priority, description, status, assignee, reporter):
        id = 1
        while id in self.used_task_ids:
            id += 1
        self.used_task_ids.add(id)
        new_task = Task(id, title, priority, description, status, assignee, reporter)
        self.tasks.append(new_task)
        print("\nTask added successfully\n")
        return new_task

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.used_task_ids.remove(task_id)
                print("\nTask deleted successfully\n")
                return
        print("\nTask not found\n")

    def change_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.id == task_id:
                task.change_status(new_status)
                print("\nTask status changed successfully\n")
                return
        print("\nTask not found\n")
    
    def change_task_priority(self, task_id, new_priority):
        for task in self.tasks:
            if task.id == task_id:
                task.change_priority(new_priority)
                print("\nTask priority changed successfully\n")
                return
        print("\nTask not found\n")

    def printBoard(self):
        print("\nProject Name: ", self.Project_name)
        print("Created By: ", self.created_by)
        print("\nTasks:")
        for task in self.tasks:
            print("\nTask ID: ", task.id)
            print("Title: ", task.title)
            print("Priority: ", task.priority)
            print("Description: ", task.description)
            print("Status: ", task.status)
            print("Assignee: ", task.assignee)
            print("Reporter: ", task.reporter)
            print("Time Started: ", task.time_started)
            print("Time Finished: ", task.time_finished)
            print("Time Taken: ", task.time_taken)
            print("\n")
class Boards:
    boards=[]
    def __init__(self):
        pass
    def add_project(self, project):
        self.boards.append(project)

projects = Boards()
while True:
    user = input("Enter '1' to create a new project, '2' to add a new task, '3' to delete a task, '4' to change task status, '5' to change task priority, '6' to print board, '7' to exit: ")
    if user == '1':
        project = KBoard(1, "", "")
        project.Project_name = input("Enter project name: ")
        project.created_by = input("Enter your name: ")
        projects.add_project(project)

    elif user == '2':
        title = input("Enter task title: ")
        priority = input("Enter task priority: ")
        description = input("Enter task description: ")
        status = input("Enter task status: ")
        assignee = input("Enter task assignee: ")
        reporter = input("Enter task reporter: ")
        project.add_new_task(1, title, priority, description, status, assignee, reporter)
    elif user == '3':
        id = int(input("Enter the task id to delete: "))
        project.delete_task(id)
    elif user == '4':
        id = int(input("Enter the task id to change status: "))
        new_status = input("Enter the new status: ")
        project.change_task_status(id, new_status)
    elif user == '5':
        id = int(input("Enter the task id to change priority: "))
        new_priority = input("Enter the new priority: ")
        project.change_task_priority(id, new_priority)
    elif user == '6':
        project.printBoard()
    elif user == '7':
        Confirm = input("Are you sure you want to exit? (y/n): ")
        if Confirm.lower == 'y':
            break
        else:
            continue
    else:
        print("Invalid Option! Please try again.")

exit()