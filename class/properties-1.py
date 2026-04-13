class Person():
    
    def __init__(self,name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name cannot empty")
        
person1 = Person("Alice")
print(person1.name)
person1.name = "raj"
print(person1.name)