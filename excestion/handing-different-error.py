try:
    print("enter the no")
    age = int(input("enter your age"))
    x = 10/age
except (ZeroDivisionError, ValueError):
    print("print it any error")
print("excesption has continous")    