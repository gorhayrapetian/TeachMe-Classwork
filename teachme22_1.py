from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "DOB"])

li = ["Gor", "17", "02.05.2005"]

di = {'name': 'Mikhail', 'age': '19', 'DOB': '13.09.1999'}

student_1 = Student._make(li)

print(student_1)

print(Student(**di))