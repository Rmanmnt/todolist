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
    
    def check_add_task_entry_values(self, name, description, priority,status):
        if not name.strip():
            return False, "Name is required."
        if len(name) < 3:
            return False, "Name must be at least 3 characters."
        if not description.strip():
            return False, "Description is required."
        if priority not in ["کم", "متوسط", "زیاد"]:
            return False, "Priority is invalid."
        if status not in ["فعال", "غیرفعال", "تمام شده"]:
            return False, "status is invalid."
        return True, ""
        
    
    def get_task(self,task_id):
        return self.to_do_list.show_task(task_id)
    
    def update_task(self, id, name, description, priority, status):
        if self.to_do_list.check_repetitive_name(name,id):
            return f"Task '{name}' already exists."
        result=self.to_do_list.update_task(id, name, description, priority, status)
        return result

