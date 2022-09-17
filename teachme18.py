class Person:
    def __init__(self, name, age): # self is the name of the class
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Name {self.name}\nAge {self.age}'

person = Person('John', 24)
print(person)

person_1 = Person('Garnik', 20)
print(person_1)

print(person.age != person_1.age)