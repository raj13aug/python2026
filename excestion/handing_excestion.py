try:
    age = int(input("enter your age"))
except ValueError as error:
    print("you enter wrong number")    
    print(error)
    print(type(error))
else:
    print(" No excepection were thrown")    
print("excution continous")    
    