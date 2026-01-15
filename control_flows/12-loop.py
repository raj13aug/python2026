number = 100

while number:
    print(number)
    number //= 2
    
    
command = ""    

while command != "quit" and command !="QUIT":
    x = input(">")
    print("echo", x)

command = ""
while command.lower() != "quit":
    command = input(">")
    print("command")