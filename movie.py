class Movie:
    
    def __init__(self,name,director,year):
        self.name = name
        self.director = director
        self.year = year
        
        
    def __str__(self):
        return self.name +" " + self.year +" " + "directed by" +" "+ self.director
        
    def recent(self):
        if self.year == 2018:
            return True
        else:
            return False
            
Movie1 = Movie("Goal","Danny Cannon", "2005" )

print(Movie1.name,Movie1.director, Movie1.year)
print(Movie1.__str__())
print(Movie1.recent())