items = [
    ("product2", 30),
    ("product4", 500),
    ("product6", 100)
]


prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >=100]
print(prices)
print(filtered)