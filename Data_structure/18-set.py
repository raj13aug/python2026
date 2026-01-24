# Set is unorder collection of unique items, we cannot have a duplicate, and object are unordered they are in sequence, so we cannot access from index method. 


numbers = [1,2,3,4]
x = set(numbers)
print(x)
print(type(x))

frist = {1,3,5}
second = {2,4,6}

union = (frist | second)
print(union)
union = (frist & second)
print(union)
union = (frist ^ second)
print(union)
union = (frist - second)
print(union)
