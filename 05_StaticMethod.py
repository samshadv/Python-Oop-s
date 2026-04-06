#A static method belongs to the class but does not use instance (self) or class (cls) data.

class Car:
     count = 0
     
     def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.count += 1
        
     @staticmethod
     def general_description():
        return "Cars are vehicles used for transportation."
    
car1 = Car("Toyota", "Fortuner", 2022)
car2 = Car("Tesla", "Model S", 2023)

print(Car.general_description())
    
    
