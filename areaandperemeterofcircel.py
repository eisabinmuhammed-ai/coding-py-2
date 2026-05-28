import math

class Circle:
    
    pi = math.pi 

    def __init__(self, radius):
     
        self.radius = radius

    def calculate_perimeter(self):
      
        return 2 * self.pi * self.radius

    def calculate_area(self):
      
        return self.pi * (self.radius ** 2)



my_circle = Circle(5)


perimeter = my_circle.calculate_perimeter()
area = my_circle.calculate_area()

print(f"For a circle with radius {my_circle.radius}:")
print(f"Perimeter (Circumference): {perimeter:.2f}")
print(f"Area: {area:.2f}")