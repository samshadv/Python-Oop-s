#A class variable is shared by all objects of a class.

class Car:
    total_car = 0   

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.total_car += 1   

car1 = Car("Toyota", "fortuner", 2022)
car2 = Car("Toyota", "fortuner", 2023)
car3 = Car("Toyota", "fortuner", 2024)

print(Car.total_car)