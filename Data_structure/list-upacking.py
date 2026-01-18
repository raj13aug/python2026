numbers = list(range(10))

first, second, *other = numbers
print(*other)

first, *other, last = numbers
print(last)