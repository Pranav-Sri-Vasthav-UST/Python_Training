from student_manager import StudentManager
from storage import Storage

def display_students(students: list) -> None:
    if not students:
        print("No students to display")
    else:
        for stu in students:
            print(f"{stu.id} - {stu.name} - Age: {stu.age} - Grade: {stu.grade}")

def main():
    manager = StudentManager()
    store = Storage()

    saved_students = store.load()
    manager.load_students(saved_students)

    while True:
        print("\nStudent Application: ")
        print("1. Add student\n2. View all students\n3. Search student by ID\n4. Delete student\n5. Exit")
        choice = input("\nChoice -> ")

        if choice == '1':
            name = input("Enter a name: ")
            if name.strip():
                try:
                    age = int(input("Enter age: "))
                    grade = input("Enter grade (optional): ")
                    grade = grade if grade.strip() else None
                    
                    stu = manager.add_student(name.strip(), age, grade)
                    store.save(manager.to_dict_list())
                    print(f"Student added with ID: {stu.id}")
                except ValueError:
                    print("Age must be a number")
            else:
                print("Name cannot be empty")
        elif choice == '2':
            display_students(manager.get_all_students())
        elif choice == '3':
            search_id = input("Enter student ID to search: ")
            student = manager.find_student_by_id(search_id)
            if student:
                print(f"\nStudent found:")
                print(f"ID: {student.id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
            else:
                print("No student found with that ID")
        elif choice == '4':
            sid = input("Enter the Student ID to delete: ")
            if manager.delete_student(sid):
                store.save(manager.to_dict_list())
                print("Student Deleted")
            else:
                print("Student ID not found")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":

    main()