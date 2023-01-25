from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "DOB", "teachers"])

student_1 = Student("Gor", "17", "02/05/2005", ["r. Brown", "Mrs. Nancy"])

print(student_1[0]) # name

print(student_1.age)

print(getattr(student_1, "DOB"))

student_1.teachers.append("Vardan Ghukasyan")

print(student_1) 