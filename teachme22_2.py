from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "DOB"]) 

student_1 = Student("Gor", "17", "02/05/2005")

print(Student._fields)

print(student_1._replace(name='Hamlet'))