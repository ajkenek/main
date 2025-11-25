class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

student1 = Student("", [60, 90, 40])
student2 = Student("", [50, 50, 40])

print(student1.is_passed())
print(student2.is_passed())