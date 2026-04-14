
class Human:
    def rest(self):
        return "Sleeping"    

class Robot:
    def rest(self):
        return "Robot recharges battery for 2 hours."
    
 
def take_rest(entity):
     print(entity.rest())
     
# Create objects
human = Human()  # Inherits from Animal
robot = Robot()

# Call the function for both objects
take_rest(human)  # Works because Human has rest()
take_rest(robot)       