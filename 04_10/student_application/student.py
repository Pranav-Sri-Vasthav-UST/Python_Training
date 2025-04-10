import uuid
class Student:

    def __init__(self, name: str, age, grade:str = None, stu_id = None):
        self.id = stu_id if stu_id else str(uuid.uuid4())
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(
            stu_id=data["id"],
            name = data["name"],
            age = data["age"],
            grade = data["grade"]
        )