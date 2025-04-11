from employee_manager import EmployeeManager
from storage import Storage

def display_employees(employees):
    if not employees:
        print("No employees found.")
    for e in employees:
        print(e)

def main():
    manager = EmployeeManager()
    storage = Storage("employees.pkl") #initialize storage with loaded data

    saved_data = storage.load()
    manager.load_employees(saved_data)

    while True:
        print("\n1. Add Employee\n2. View All\n3. Search by ID\n4. Delete Employee\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            department = input("Department: ")
            designation = input("Designation: ")
            try:
                gross_salary = float(input("Gross Salary: "))
                tax = float(input("Tax: "))
                bonus = float(input("Bonus: "))
            except ValueError:
                print("Please enter valid numeric values for salary, tax, and bonus.")
                continue

            # add the employee and save the updated data
            employee = manager.add_employee(name, department, designation, gross_salary, tax, bonus)
            storage.save(manager.to_dict_list())
            print(f"Employee added with ID: {employee.id}")

        # Display all the images
        elif choice == '2':
            display_employees(manager.get_all_employees())

        # search by employee ID
        elif choice == '3':
            eid = input("Enter employee ID: ")
            employee = manager.find_by_id(eid)
            if employee:
                print(employee)
            else:
                print("Employee not found.")
        
        # delete an employee by ID
        elif choice == '4':
            eid = input("Enter employee ID: ")
            if manager.delete_employee(eid):
                storage.save(manager.to_dict_list())
                print("Employee deleted.")
            else:
                print("Employee not found.")

        # exit the application
        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
