#Polymorphism means one method name can have different behaviors in different classes.

class Car:
   
    def fuel_type(self):
        return "This car uses petrol or diesel."
        

class ElectricCar(Car):
    def fuel_type(self):
        return "This car uses electricity."


car1 = Car("Toyota","Sarari")
car2 = ElectricCar("Tesla")


print(car1.fuel_type())
print(car2.fuel_type())
