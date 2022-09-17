class Animal:
    Type = 'chihuahua'

    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def bark(self):
        return f'I am  {self.name} and I am {self.age} years old I am {self.breed} my color is {self.color}'

    def sit(self):
        return f'The dog named {self.name} is sat'


dog_1 = Animal('Tim', 3, Animal.Type, 'green')
dog_2 = Animal('Tuzik', 2, Animal.Type, 'pink')

print(dog_1.bark())
print(dog_2.sit())
