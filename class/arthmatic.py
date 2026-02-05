# class Point:
    
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
    
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
# point = Point(1,4)    
# other = Point(1,5)

# combined = point + other
# print(combined)


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    

point = Point(1, 4)    
other = Point(1, 5)

combined = point + other
print(combined)