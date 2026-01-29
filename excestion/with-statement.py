try:
    age = int(input("enter your age"))
    with open("file.py") as file:
        print("files is open")
except ValueError as error:
    print("you enter wrong number")    
    print(error)
    print(type(error))
else:
    print(" No excepection were thrown")