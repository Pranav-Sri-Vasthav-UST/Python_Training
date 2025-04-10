from student import Student

class StudentManager(object):

    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade=None):
        student = Student(name, age, grade)
        self.students.append(student)
        return student
    
    def get_all_students(self):
        return self.students

    def delete_student(self, stu_id):
        for stu in self.students:
            if stu.id == stu_id:
                self.students.remove(stu)
                return True
        return False
    
    def find_student_by_id(self, stu_id):
        for student in self.students:
            if student.id == stu_id:
                return student
        return None

    def load_students(self, student_dicts):
        self.students = [Student.from_dict(sd) for sd in student_dicts]

    def to_dict_list(self):
        return [stu.to_dict() for stu in self.students] 