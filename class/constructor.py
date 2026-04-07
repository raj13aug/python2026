# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
        
#     def draw(self):
#         print(f"point ({self.x} {self.y})")
        
# point = Point(1, 3) 
# print(point.x)
# point.draw()


class Hello():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"what is your name {self.x}, which class is studing {self.y}")
        

z = Hello(1,3)
z.draw()