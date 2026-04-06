#property decorator (@property) is used to control access to class attributes.

class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.__model = model   
        self.year = year
        
    @property
    def model(self):
        return self.__model
        
car1 = Car("Toyota", "Fortuner", 2022)

print(car1.model)