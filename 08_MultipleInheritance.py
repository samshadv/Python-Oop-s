class Car:
    def class_info(self):
        return "This is car"
    
class Engine:
    def engine_info(self):
        return "this is engine"
    
class Battery:
    def battery_info(self):
        return "this is battery"
    
class ElectricCar(Car, Engine, Battery):
    def car_info(self):
        return "This is an electric car."
    
my_tesla = ElectricCar()

print(my_tesla.class_info())
print(my_tesla.engine_info())
print(my_tesla.battery_info())
