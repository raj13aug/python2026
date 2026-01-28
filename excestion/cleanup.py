try:
    age = int(input("enter your age"))
    file = open("file.py")
except ValueError as error:
    print("you enter wrong number")    
    print(error)
    print(type(error))
else:
    print(" No excepection were thrown")  
finally:
    file.close()