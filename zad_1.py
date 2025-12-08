from klasy.student import Student


student1 = Student("", [60, 90, 40])
student2 = Student("", [50, 50, 40])

print(student1.is_passed())
print(student2.is_passed())
