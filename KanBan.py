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
    
