import unittest
import os
from employee import Employee
from storage import Storage

class TestStorage(unittest.TestCase):
    
    # Setting up test data
    def setUp(self):
        self.filepath = "D:\Python Training\Python_Training\employees.pkl"
        self.storage = Storage(self.filepath)
        self.employee1 = Employee("Pranav", "IT", "Developer", 85000, 10000, 5000)
        self.employee2 = Employee("Aleena", "HR", "Manager", 95000, 12000, 8000)
        self.employees = [self.employee1, self.employee2]

    # clean up after each test to remove test files
    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    # testing that saving and loading employees works correctly
    def test_save_and_load(self):
        self.storage.save(self.employees)
        self.assertTrue(os.path.exists(self.filepath))

        loaded_employees = self.storage.load()
        self.assertEqual(len(loaded_employees), 2)
        self.assertEqual(loaded_employees[0].name, "Pranav")
        self.assertEqual(loaded_employees[1].name, "Aleena")

    # testing loading from a file that doesn't exist returns empty list
    def test_load_nonexistent_file(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        result = self.storage.load()
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
