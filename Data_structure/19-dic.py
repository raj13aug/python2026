point = {"a":1,"y":2}
dict() # create the empty string
new = dict(a=1,b=2)
print(new)
new["x"] = 3
print(new)

if "x" in new:
    print("I am here")
  
print(point.get("x")) # if value doesn't exit print none 
print(point.get("x", 0)) # if value doesn't exit then print zero instead of none

for key in point:
    print(key, point[key])


for key,value in point.items()    :
    print(key,value)
    
del point["y"]
print(point)
