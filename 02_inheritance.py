#Inheritance allows one class to acquire properties and methods of another class.
from car import Car

class ElectricCar(Car):
    def __init__(self,brand,model,year,battery_size):
        super().__init__(brand,model,year)
        self.battery_size = battery_size
        
my_car = ElectricCar("Tesla","Model S","2023","85kWh")
print(my_car.battery_size)
my_car.drive()