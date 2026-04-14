from abc import ABC, abstractmethod

class MyAbstract(ABC):
    
    @staticmethod
    @abstractmethod
    def hell():
        pass
    

class Game(MyAbstract):
    
    @staticmethod
    def hell():
        print("hello boy")


# you can call static method directly
Game.hell()