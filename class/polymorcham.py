class Animal:
    def walk(self):
        return "Animal is walking"
    

class Lion(Animal):
    def walk(self):
        return "lion is walking"
    
class Monkey(Animal):
    def walk(self):
        return "Money is walking"
    
    
monkey =  Monkey()   
lion = Lion()

print(monkey.walk())
print(lion.walk())
    