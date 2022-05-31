import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return float(self.radius) ** float(2) * math.pi

    def get_circumference(self):
        return float(self.radius) * float(2) * math.pi
