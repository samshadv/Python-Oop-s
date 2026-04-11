# Create a class Car with attributes brand and model. Print them.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model= model
        
c1 = Car("Toyota", "Corolla")
print(c1.model,c1.brand)