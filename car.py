class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        

    def drive(self):
        print(f"You drive the {self.brand}")
        
    def stop(self):
        print(f"You stop the {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.brand} {self.model}")