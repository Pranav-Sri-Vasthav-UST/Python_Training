import pickle
import os

class Storage:

    # initialize with a filepath for storing employee data
    def __init__(self, filepath="employees.pkl"):
        self.filepath = filepath

    # save a list of employee dicts to pickle file
    def save(self, employee_list):
        with open(self.filepath, "wb") as f:
            pickle.dump(employee_list, f)

    # load from the pickle file 
    def load(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "rb") as f:
            return pickle.load(f)
