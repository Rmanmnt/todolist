import uuid

class Task():

    def __init__(self,name,description,priority,status=None,id=None):
        self.id =id or str(uuid.uuid4())
        self.name = name
        self.description = description
        self.priority = priority
        self.status =status or 'فعال'

    def __str__(self):
        return self.name
    # \ndescription: {self.description}\npriority: {self.priority}