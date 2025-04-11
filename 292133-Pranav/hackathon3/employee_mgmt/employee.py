import uuid

class Employee:
    # initialize new employee object with provided details and new uuid will be generated
    def __init__(self, name, department, designation, gross_salary, tax, bonus, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.calculate_net_salary()

    # net salary will be calculated here
    def calculate_net_salary(self):
        return self.gross_salary - self.tax + self.bonus

    # employee object is getting converted into dictionary for serialization
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }

    # create an employee obj from dictionary
    @staticmethod
    def from_dict(data):
        return Employee(
            id=data.get("id"),
            name=data["name"],
            department=data["department"],
            designation=data["designation"],
            gross_salary=data["gross_salary"],
            tax=data["tax"],
            bonus=data["bonus"]
        )

    # formatting string for representation
    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Designation: {self.designation}\n"
            f"Gross Salary: {self.gross_salary}\n"
            f"Tax: {self.tax}\n"
            f"Bonus: {self.bonus}\n"
            f"Net Salary: {self.net_salary}\n"
        )


# for self-test

if __name__ == "__main__":
    emp = Employee("pranav", "IT", "Developer", 80000, 10000, 5000)
    print(emp)


