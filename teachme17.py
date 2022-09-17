from abc import ABC

class Animal(ABC):
    
    def Action(self):
        pass

class Human(Animal):

    def action(self):
        return 'I can walk'

class Lion(Animal):

    def action(self):
        return 'I can roar'


class Snake(Animal):

    def action(self):
        return 'I can cawl'

human_object = Human()

snake_object = Snake()

lion_object = Lion()

list_with_animals = [human_object, snake_object, lion_object]

for animal_object in list_with_animals:
    print(animal_object.action())