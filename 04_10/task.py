import uuid
class Task:

    def __init__(self, description: str, completed: bool = False, task_id = None):
        self.id = task_id if task_id else str(uuid.uuid4())
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            description=data["description"],
            completed = data["completed"],
            task_id = data["id"]
        )