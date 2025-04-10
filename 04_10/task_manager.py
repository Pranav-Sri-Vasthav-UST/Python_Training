from task import Task

class TaskManager(object):

    def __init__(self):
        self.tasks = []

    # add a task
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        return task
    
    # get all tasks
    def get_all_tasks(self):
        return self.tasks

    # complete a task
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                return True
        return False

    # delete a task
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    # load tasks
    def load_tasks(self, task_dicts):
        self.tasks = [Task.from_dict(td) for td in task_dicts]

    # list of tasks in dictionary format
    def to_dict_list(self):
        return [task.to_dict() for task in self.tasks] 