class String:
    
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"value x is ({self.x}), and value y is ({self.y})"
    
point = String(1,3)
print(point)
    
