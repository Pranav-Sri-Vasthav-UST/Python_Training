import json
import os

class Storage(object):

    def __init__(self, filepath='tasks.json'):
        self.filepath = filepath

    def save(self, task_list):
        with open(self.filepath, 'w') as f:
            json.dump(task_list, f, indent=4)

    def load(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath) as f:
            return json.load(f)