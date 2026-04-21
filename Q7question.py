# #define a student class with attributes as name percentage phone no and team include the n init method to inelitize the details

class Student:
    
    def __init__(self,name,percent,phone,grade,team):
        self.name = name
        self.percent = percent
        self.phone = phone
        self.grade = grade 
        self.team = team
 
        
    def student_detail(self):
        return f"{self.name} is in {self.grade} grade with {self.percent}% from the team {self.team} having phone number {self.phone}"
    
s1 = Student("samshad", 90,8423339161,"A","A")
print(s1.student_detail())
s2 = Student("shivam", 92,8423339162,"A","B")
print(s2.student_detail())
s3 = Student("rohit", 93,8423339163,"B","C")
print(s3.student_detail())
s4 = Student("vishal", 80,8423339164,"A","C")
print(s4.student_detail())
s5 = Student("sahil", 89,8423339165,"B","B")
print(s5.student_detail())
