class Car():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x},{self.y}"
    
    def __add__(self,other):
        return (self.x + other.x, self.y + other.y)
    
    
v1 = Car(1,3)
v2 = Car(2,3)
print(v1 + v2)


# __getitem__

class CustomDict():
    
    def __init__(self,data):
        self.data = data
        
    def __getitem__(self, key):
        return self.data.get(key, "key is not found")
    
mydict = CustomDict({"name":"raj","age":"90"})
print(mydict["name"])


class Equa():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
point1 = Equa(1,2)
point2 = Equa(1,2)
    
print(point1 == point2)
    
        