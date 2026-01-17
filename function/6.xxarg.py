def mutiply(*numbers):
    total = 1
    for value in numbers:
        total *= value
    return total

print(mutiply(2,3,4,5))