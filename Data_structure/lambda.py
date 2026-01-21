item = [
    ("product2", 30),
    ("product4", 500),
    ("product6", 100)
]

# lambda  parameter:experssion

# lambda function doesn't required the def function

item.sort(key=lambda item: item[1])
print(item)