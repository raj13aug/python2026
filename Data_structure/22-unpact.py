value = [1,2,3,4]
print(value)
print(*value)


v1 = {"x":2}
v2 = {"y":5}

# unpack you can combine both any object
combined = {**v1, **v2}
print(combined)


v1 = [1,2]
v2 = [3,4]

combined = [*v1, *v2]
print(combined)