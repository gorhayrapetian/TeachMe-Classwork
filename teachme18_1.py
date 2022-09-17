class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __repr__(self):
        return f'The person is {self.age} years old.'

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        return False

    def __gt__(self, other):
        if self.age > other.age:
            return True 
        return False

    def __lt__(self, other):
        if self.age < other.age:
            return True
        return False

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __truediv__(self, other):
        print(self.age, other.age)
        return self.age / other.age

    def __mul__(self, other):
        return self.age * other.age

    def __ge__(self, other):
        if self.age >= other.age:
            return True
        return False

    def __lte__(self, other):
        if self.age <= other.age:
            return True
        return False

person_1 = Person('Gor', 17)

person_2 = Person('Samvel', 24)

print(person_1)

print(person_1 == person_2)

print(person_1 < person_2)

print(person_1 < person_2) 

print(person_1 + person_2)

print(person_1 - person_2)

print(person_1 / person_2)

print(person_1 * person_2)

print(person_1 >= person_2)

print(person_1 <= person_2)