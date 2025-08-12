from core.to_do_list import ToDoList

class ToDoController:
    def __init__(self):
        self.to_do_list = ToDoList()

    def add_task(self, name, description, priority,status):
        result = self.to_do_list.add_task(name, description, priority, status)
        return result

    def remove_task(self, task_id):
        result = self.to_do_list.remove_task(task_id)
        return result

    def get_all_tasks(self):
        return list(self.to_do_list.show_all_tasks())
    
    def check_add_task_entry_values(self, name, description, priority):
        if not name.strip():
            return False, "Name is required."
        if len(name) < 3:
            return False, "Name must be at least 3 characters."
        if not description.strip():
            return False, "Description is required."
        if priority not in ["کم", "متوسط", "زیاد"]:
            return False, "Priority is invalid."
        return True, ""
        
    
    def get_task(self,task_id):
        return self.to_do_list.show_task(task_id)
