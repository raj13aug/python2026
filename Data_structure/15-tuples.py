# end of string ","
value = 1,
print(value)
# empty typles
value = tuple()
print(type(value))
# empty tuples
value = ()
print(type(value))
# convert to tuples
value = tuple([1,2,3])
print(value)
# mutpliy by 2
value = (1,3) * 2
print(value)
# add both tuples (concatenate)
value = (1,2) + (3,4)
print(value)

#assign the number
x, y , z, u = value
print(x)

if 2 in value:
    print("yes")
    