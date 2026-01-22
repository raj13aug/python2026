items = [
    ("product2", 30),
    ("product4", 500),
    ("product6", 100)
]

filter = list(filter(lambda item: item[1] >= 35, items))
print(filter)