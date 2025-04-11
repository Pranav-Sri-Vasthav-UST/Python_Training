import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    # setting-up the test data
    def setUp(self):
        self.employee = Employee(
            name="Pranav",
            department="IT",
            designation="Analyst",
            gross_salary=85000,
            tax=12000,
            bonus=7000
        )

    # Testing the Employee objs with proper attributes
    def test_initialization(self):
        self.assertEqual(self.employee.name, "Pranav")
        self.assertEqual(self.employee.department, "IT")
        self.assertEqual(self.employee.designation, "Analyst")
        self.assertEqual(self.employee.gross_salary, 85000)
        self.assertEqual(self.employee.tax, 12000)
        self.assertEqual(self.employee.bonus, 7000)
        self.assertEqual(self.employee.net_salary, 85000 - 12000 + 7000)

    # testing the to_dict that converts employee to dict
    def test_to_dict(self):
        data = self.employee.to_dict()
        self.assertEqual(data["name"], "Pranav")
        self.assertEqual(data["net_salary"], 85000 - 12000 + 7000)
        self.assertIn("id", data)

    # testing the from_dict that creates employee objects from dict data
    def test_from_dict(self):
        data = {
            "id": "test-id-456",
            "name": "Aleena",
            "department": "IT",
            "designation": "Developer",
            "gross_salary": 95000,
            "tax": 15000,
            "bonus": 8000,
            "net_salary": 88000
        }
        emp = Employee.from_dict(data)
        self.assertEqual(emp.id, "test-id-456")
        self.assertEqual(emp.name, "Aleena")
        self.assertEqual(emp.net_salary, 88000)

if __name__ == "__main__":
    unittest.main()
