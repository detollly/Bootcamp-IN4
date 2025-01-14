class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"Student: {self.name}"

new_student = Student('Calum', 20, 'A')

print(new_student.name)