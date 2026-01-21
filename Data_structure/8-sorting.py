numbers = [1,4,6,9,10]

print(numbers.sort(reverse=True))
print(sorted(numbers, reverse=True))



item = [
    ('product1', 10),
    ('product7', 20),
    ('product8', 90),
]

# for val in numbers:
#     print(val[1])
    
    
def item_sorts(items):
    return items[1]

item.sort(key=item_sorts)
print(item)

    


