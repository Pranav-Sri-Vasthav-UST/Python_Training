import unittest
from student_manager import StudentManager

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()
    
    def test_add_student(self):
        name = "anil"
        age = 12
        grade = "6"
        initial_count = len(self.manager.students)
        student = self.manager.add_student(name, age, grade)
        self.assertEqual(len(self.manager.students), initial_count + 1)
        self.assertEqual(self.manager.students[-1].name, name)
        self.assertEqual(self.manager.students[-1].age, age)
        self.assertEqual(self.manager.students[-1].grade, grade)
        
        self.assertEqual(student.name, name)
        self.assertEqual(student.age, age)
        self.assertEqual(student.grade, grade)

if __name__ == "__main__":
    unittest.main()
