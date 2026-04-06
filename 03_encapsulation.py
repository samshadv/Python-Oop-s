#Encapsulation means wrapping data (variables) and methods into a single unit (class) and restricting direct access
class Car:
    def __init__(self,brand,model,year):
        self.__brand = brand
        self.model = model
        self.year = year
        
    def get_brand(self):
        return self.__brand
    
car1 = Car("Toyota","fortuner",2022)

print(car1.get_brand())