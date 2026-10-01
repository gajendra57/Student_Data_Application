class Student: 
    def __init__(self,name,roll,standard):
        self.name=name 
        self.roll=roll 
        self.standard=standard 

    def display(self): 
        return f"name:{self.name},roll:{self.roll},class:{self.standard}" 

# s1=Student("dilkush",2,2)
# print(s1.display())