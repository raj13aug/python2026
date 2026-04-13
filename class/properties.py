class Price():
    
    def __init__(self,price):
        self.set_price(price)
    
    def get_price(self):
        return self.__price()
        
    def set_price(self,value):
        if value < 0:
            raise ValueError("price is negetive")
        self.__price = value
        
p = Price(10)        