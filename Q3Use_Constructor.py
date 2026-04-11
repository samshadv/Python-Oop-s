# Create a class Rectangle to find area.

class Rectangle:
    
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
        
    def area(self):
        print(self.length*self.breath)
        
r1 = Rectangle(3,5)
r1.area()