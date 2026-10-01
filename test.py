from student import Student 
from storage import save_student,load_data  
s1=Student("abc",2,2)
s2=Student("efg",3,3)   
s3=Student("Chandan",4,4)
save_student(s1) 
save_student(s2)
save_student(s3) 
#load 
load_data()
