item = [
    ("product2", 30),
    ("product4", 500),
    ("product6", 100)
]


value = list()

for items in item:
    value.append(items[1])
print(value)


# https://www.datacamp.com/tutorial/python-map-function


'''
To a list: list(map(function, iterable))

To a set: set(map(function, iterable))

Iterate directly: for item in map(function, iterable): ..

'''
items = [
    ("product2", 30),
    ("product4", 500),
    ("product6", 100)
]

x = list(map(lambda item: item[1], items))
print(x)