class student:
    
    def __init__(self,fname,lname,phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        
    def get_student(self):
        return self.fname 
        
    def get_students(self):
        return self.lname
        
    def get_studentss(self):
        return self.phone

stu1 = student('Tom','Smith','85641265')

print(stu1.get_student())
print(stu1.get_students())
print(stu1.get_studentss())