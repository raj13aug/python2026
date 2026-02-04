class Car:
    
    total_car = 0 # class method
    
    def __init__(self, brand, model):
        self.car = brand
        self.model = model
        
    def display_info(self):
        print(f"{self.car} {self.model}")
        Car.total_car += 1
        
    @classmethod
    def display_car_count(cls):
        print(f"Total car count: {cls.total_car}")

my_car = Car("mitsuble", 2012)
my_car.display_info()
Car.display_car_count()

