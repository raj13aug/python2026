
#It will generator key:value of dic
value = { x : x * 2 for x in range(5)}
print(value)

# It will generator object 
value = (x * 2 for x in range(5))
print(value)