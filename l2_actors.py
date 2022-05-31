class actor:
    
    def __init__(self,fullname,salary,height):
        self.fullname = fullname
        self.salary = salary
        self.height = height
        
    def get_actor(self):
        return self.fullname
        
    def get_actor1(self):
        return self.fullname +  self.salary
        
    def get_actor2(self):
        return self.fullname + self.salary + self.height
        
actor1 = actor('Tom Hanks','','')
actor2 = actor('Denzel Washington', 120000, '')
actor3 = actor('Johnny Depp', 110000, 178)

print(actor2)