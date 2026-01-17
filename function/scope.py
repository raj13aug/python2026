message = "a"

def hello(name):
    message = "b"
    print("value comes from", message)
    
hello("raj")   
print(message)

# if you want to overright the local variable then use global

def hello1(name):
    global message
    message = "a"
    print("value from inside the hello1", message)
    
    
hello1("happy")