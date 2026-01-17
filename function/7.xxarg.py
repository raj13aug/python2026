def collection(**argument):
    print(argument)
    
collection(id=1,name='raj',age=40)

def collection(*argument):
    print(argument)
    
collection(1,2,3)

# **argument → Dictionary (dict)
# *argument → Tuple (tuple)