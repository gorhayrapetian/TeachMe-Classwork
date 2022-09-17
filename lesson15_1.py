brand = str(input('Enter the car brand: '))
engine = input('Enter the volume of car engine: ')
turbo = str(input('Enter the turbo type: '))
horsepower = int(input('Enter the number of horsepower the car has: '))
torque = int(input('Enter the pound feet of torque the car has: '))
seats = int(input('Enter the number of seats: '))


class Vehicle:
    def __init__(self, brand, engine, turbo, horsepower, torque):
        self.brand = brand
        self.engine = engine
        self.turbo = turbo
        self.horsepower = horsepower
        self.torque = torque

    def get_car_model(self):
        return (f'This {self.brand} has {self.engine}L {self.turbo} engine with {self.horsepower} horsepower, {self.torque} pound feet of torque and {self.seats} seats.')


class Car(Vehicle):
    def __init__(self, brand, engine, turbo, horsepower, torque, seats):
        super().__init__(brand, engine, turbo, horsepower, torque, )
        self.seats = seats


b = Car(brand, str(engine), turbo, horsepower, torque, seats)

print(b.get_car_model())
