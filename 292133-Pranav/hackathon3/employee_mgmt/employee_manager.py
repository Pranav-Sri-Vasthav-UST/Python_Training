from employee import Employee

class EmployeeManager:

    # initialize the employeemanager with an empty list
    def __init__(self):
        self.employees = []

    # creates and add new employees with the details
    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        employee = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employees.append(employee)
        return employee

    # returns all the managers
    def get_all_employees(self):
        return self.employees

    # returns employee by given id
    def find_by_id(self, employee_id):
        return next((e for e in self.employees if e.id == employee_id), None)

    # deletes employee by given id
    def delete_employee(self, employee_id):
        employee = self.find_by_id(employee_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False

    # load employees from the list
    def load_employees(self, employee_dicts):
        self.employees = [Employee.from_dict(d) for d in employee_dicts]

    # converts all employees to list of dicts
    def to_dict_list(self):
        return [e.to_dict() for e in self.employees]

# for self testing
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.add_employee("pranav", "IT", "Developer", 80000, 10000, 5000)
    for emp in manager.get_all_employees():
        print(emp)
