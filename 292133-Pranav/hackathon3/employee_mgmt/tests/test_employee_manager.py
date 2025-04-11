import unittest
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):

    # setting up test data
    def setUp(self):
        self.manager = EmployeeManager()
        self.pranav = self.manager.add_employee("Pranav", "IT", "Analyst", 85000, 12000, 7000)
        self.aleena = self.manager.add_employee("Aleena", "HR", "Manager", 95000, 15000, 8000)

    # testing that employees are added correctly
    def test_add_employee(self):
        self.assertEqual(len(self.manager.employees), 2)
        self.assertEqual(self.pranav.name, "Pranav")
        self.assertEqual(self.pranav.net_salary, 85000 - 12000 + 7000)

    # the get_all_employees method is being tested
    def test_get_all_employees(self):
        all_emps = self.manager.get_all_employees()
        self.assertEqual(len(all_emps), 2)
        self.assertIn(self.aleena, all_emps)

    # testing finding employees by ID
    def test_find_by_id(self):
        found = self.manager.find_by_id(self.pranav.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Pranav")

        not_found = self.manager.find_by_id("fake-id")
        self.assertIsNone(not_found)

    # testing employee deletion
    def test_delete_employee(self):
        result = self.manager.delete_employee(self.aleena.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.employees), 1)

        result = self.manager.delete_employee("nonexistent-id")
        self.assertFalse(result)

    # testing serialization and deserialization of employees
    def test_load_and_to_dict_list(self):
        dict_list = self.manager.to_dict_list()
        new_manager = EmployeeManager()
        new_manager.load_employees(dict_list)

        self.assertEqual(len(new_manager.employees), 2)
        self.assertEqual(new_manager.employees[0].name, "Pranav")
        self.assertEqual(new_manager.employees[1].name, "Aleena")

if __name__ == "__main__":
    unittest.main()
