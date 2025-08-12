import csv
from .task import Task

class ToDoList:
    def __init__(self):
        self.Tasks = []
        self.load_tasks()
    
    def add_task(self, name,description,priority,status):
        task = Task(name,description,priority,status)
        for t in self.Tasks:
            if t.name == task.name:
                return f"Task '{task.name}' already exists."
        self.Tasks.append(task)
        self.save_tasks()
        return f"Task '{task.name}' added."
    
    def remove_task(self, task_id):
        for task in self.Tasks:
            if task.id == task_id:
                self.Tasks.remove(task)
                self.save_tasks()
                return f"Task {task.name} removed"
        return f"Task was not found"
    
    def save_tasks(self):
        with open('save_tasks.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for task in self.Tasks:
                writer.writerow([task.id, task.name, task.description, task.priority, task.status])
    
    def show_all_tasks(self):
        for task in self.Tasks:
            yield task
    
    def show_task(self,id):
        for task in self.Tasks:
            if id == task.id:
                return task
        return None

    def load_tasks(self):
        self.Tasks.clear()
        try:
            with open('save_tasks.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 5:
                        continue
                    try:
                        id, name, description, priority ,status= row
                        task = Task(name, description, priority,status,id)
                        self.Tasks.append(task)
                    except Exception as e:
                        continue
        except FileNotFoundError:
            with open('save_tasks.csv', 'w', newline='', encoding='utf-8') as file:
                pass

    def get_id(self,name):
        for task in self.Tasks:
            if task.name == name:
                return task.id