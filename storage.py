from student import Student 
import os  
import pickle 
#creating first function 
database="student.pkl" 
students=[]
def save_student(s): 
      
    if os.path.exists(database):
        with open(database,"rb") as file: 
            data=pickle.load(file) 
            data.append(s) 
        with open(database,"wb") as file: 
            pickle.dump(data,file)
    else:
        with open(database,"wb") as file: 
            students.append(s) 
            pickle.dump(students,file)
#load data function 

def load_data(): 
    with open(database,"rb") as file: 
        data=pickle.load(file) 
        for ele in data: 
            print(ele.display())
