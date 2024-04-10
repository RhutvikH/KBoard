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
