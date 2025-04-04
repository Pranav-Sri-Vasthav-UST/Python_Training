# imports

import json
from datetime import datetime

# process


# creating the person class 
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # returns a formatted string
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    

# creating the employee class with class method and static method which returns objects
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        self.join_date = datetime.now().strftime("%Y-%m-%d")

    # creates an Employee object from a comma-separated string
    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, int(salary))
    
    # Overrides the parent method
    def get_details(self):
        return f"{self.name} ({self.emp_id}) - {self.department}, ₹{self.salary}"
    
    # calculates the bonus
    def calculate_bonus(self, percentage=10):
        if self.salary < 50000:
            return self.salary * (percentage / 100)
        return 0
    
    # Static method to display the company's bonus policy
    @staticmethod
    def bonus_policy():
        print("Standard Bonus: 10% of salary for employees with salary less than ₹50,000")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    # add an employee to the department if employee instance is there
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            return True
        return False
    
    # removes employee by id
    def remove_employee(self, emp_id):
        for i, emp in enumerate(self.employees):
            if emp.emp_id == emp_id:
                return self.employees.pop(i)
        return None
    
    # returns all employees in the current department
    def get_employees(self):
        return self.employees
    
    # calculates department average salary
    def get_average_salary(self):
        if not self.employees:
            return 0
        total = sum(emp.salary for emp in self.employees)
        return total / len(self.employees)
    
    # returns dictionary with department stats
    def get_department_details(self):
        return {
            "name": self.name,
            "employee_count": len(self.employees),
            "average_salary": self.get_average_salary()
        }

# saves the employee data to a json file
def save_to_json(employees, filename="employees.json"):
    data = []
    for emp in employees:
        emp_data = {
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        }
        if hasattr(emp, 'join_date'):
            emp_data["join_date"] = emp.join_date
        data.append(emp_data)
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# load the json data and returns employe objects
def load_from_json(filename="employees.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        
        employees = []
        for emp_data in data:
            emp = Employee(
                emp_data["name"],
                emp_data["age"],
                emp_data["gender"],
                emp_data["emp_id"],
                emp_data["department"],
                emp_data["salary"]
            )
            if "join_date" in emp_data:
                emp.join_date = emp_data["join_date"]
            employees.append(emp)
        return employees
    except FileNotFoundError:
        return []

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
        self.departments = {}
    
    # adds the employee to system and department
    def add_employee(self, employee):
        self.employees.append(employee)
        
        # add to department if it exists, otherwise create it
        if employee.department not in self.departments:
            self.departments[employee.department] = Department(employee.department)
        
        self.departments[employee.department].add_employee(employee)
        return True
    
    # removes the employee from system and department
    def remove_employee(self, emp_id):
        for i, emp in enumerate(self.employees):
            if emp.emp_id == emp_id:
                removed_emp = self.employees.pop(i)
                # Also remove from department
                if removed_emp.department in self.departments:
                    self.departments[removed_emp.department].remove_employee(emp_id)
                return removed_emp
        return None
    
    # finds by ID
    def find_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None
    
    # updates the employee and department changes 
    def update_employee(self, emp_id, **kwargs):
        emp = self.find_employee(emp_id)
        if emp:
            old_department = emp.department
            
            # update employee attributes
            for key, value in kwargs.items():
                if hasattr(emp, key):
                    setattr(emp, key, value)
            
            # if department changed, update department lists
            if 'department' in kwargs and old_department != emp.department:
                # remove from old department
                if old_department in self.departments:
                    self.departments[old_department].remove_employee(emp_id)
                
                # add to new department
                if emp.department not in self.departments:
                    self.departments[emp.department] = Department(emp.department)
                self.departments[emp.department].add_employee(emp)
            
            return True
        return False
    
    # all employees fro m  the system
    def get_all_employees(self):
        return self.employees
    
    # returns all employees from given department
    def get_employees_by_department(self, department):
        if department in self.departments:
            return self.departments[department].get_employees()
        return []
