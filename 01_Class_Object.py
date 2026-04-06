#Object = A bundle of related attributes (Variables) and Methods (functions)
#.      Ex = Phone , Cup , Car
#Class = A blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
#.      Ex = Phone = Class , Iphone 14 Pro Max = Object

from car import Car
        
car1 = Car("Toyota","fortuner",2022)
car2 = Car ("tata","safari",2020)

print(car1.brand)
print(car1.model)
print(car1.year)

car1.drive()
car2.stop()
car1.describe()
        