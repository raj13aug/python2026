letter = ["a","b","c","d"]

print(letter[3])
letter[0] = "A"
print(letter)

#slice

number = list(range(20))
print(number[0::2]) # forward order
print(number[::-1]) # reverse order