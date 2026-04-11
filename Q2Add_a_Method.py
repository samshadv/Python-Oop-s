# Create a class Student with name and marks. Add a method to display details.

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(self.name,self.marks)


s1 = Student("Rahul", 85)
s1.display()
        
        