from university import University
from student import Student

if __name__ == "__main__":
    
    university = University("Elite Academy")
    student = Student("Emma")
   
    university.add_course("Machine Learning", 4)
    university.add_course("Data Analytics", 6)
    
    university.submit_enrollment(student, "Machine Learning", 1) 
    university.submit_enrollment(student, "Data Analytics", 7)        
    
    university.process_events()



















