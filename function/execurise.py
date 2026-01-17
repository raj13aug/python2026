
# 3 --> fizz
# 5 --> buzz
# 15 3,5 --> fizzbuzz
# 7 --> same output
def fizz_buzz(input):
    if input % 3 == 0 & input % 5 == 0:
        print("fizzbuzz")
        exit
    elif input % 3 == 0:
        print("fizz")
    elif input % 5 == 0:
        print("buzz")
    else:
        print(input)        
   
fizz_buzz(1)