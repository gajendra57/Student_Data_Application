from student import Student 
from storage import save_student,load_data  
#menue 
def menu(): 
    user_input=input("Enter Your Choice:")
    if user_input=="1": 
        name=input("Enter Name:") 
        roll=input("Enter roll:")  
        std=input("Enter std:")   
        s=Student(name,roll,std) 
        save_student(s) 
    else: 
        load_data() 

menu()