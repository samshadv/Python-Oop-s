# Create two classes Father and Mother with different methods. Create Child class inheriting both.

class Father:
    
    def __init__(self):
        self.father_name ="Sirajuddin"
        self.father_age = "60"
    
    def show_father(self):
        print(f"Father's Name: {self.father_name} and he is {self.father_age} years old")
        
    def work(self):
        print("Father is working in office")
        
class Mother:
    
     def __init__(self,):
        self.mother_name ="Sahajahan"
        self.mother_age = "55"
        
     def show_mother(self):
         print(f"Mother's Name: {self.mother_name} and she is {self.mother_age} years old")
        
     def cook(self):
        print("Mother is cooking food")
        
class Child(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Mohd"
        
    def show_child(self):
        print(f"Child's Name: {self.child_name}")
        
c = Child()

c.show_child()
c.show_father()
c.show_mother()
c.work()
c.cook()          
        
        