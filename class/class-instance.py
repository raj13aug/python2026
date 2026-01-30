class human:
    human_var = "two eyes"
    def __init__(self, age, colour):
        self.age = age
        self.colour = colour
        
    def raj(self):
        skill = "python"
        print(skill)
        print(human.human_var)
        
human.human_var="Three eyes"
human1 = human(age=12,colour="red")
print(human1.raj())
        

        