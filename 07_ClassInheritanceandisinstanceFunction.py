#Inheritance is a concept where one class (child) gets the properties and methods of another class (parent).

class Car:
    
    def __init__(self, brand):
        self.brand = brand

class ElectricCar:
    
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
        
my_tesla = ElectricCar("Tesla", "100 kWh")

print(isinstance(my_tesla, ElectricCar))  
print(isinstance(my_tesla, Car))          
