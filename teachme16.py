class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        print('getter method called')
        return self.__age

    @age.setter
    def set_age(self, a):
        if a < 18:
            raise ValueError("Sorry, but your age is below 18")
        else:
            self.__age = a

person = Person()
person.set_age = 45
print(person.age)