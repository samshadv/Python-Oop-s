# Create a class Animal with method speak(). Create Dog class that inherits and overrides it.

class Animal:
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("Animal make sound ")
        
class Dog(Animal):
    
    def __init__(self,name,sound):
        super().__init__(name)
        self.sound = sound
        
    def speak(self):
        print(f"{self.name} barks: {self.sound}")
        

d = Dog("Tommy", "Woof")   
d.speak()