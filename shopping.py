shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Adds each item in the list to bill total if in stock
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total
    
print compute_bill(shopping_list), 'dollars'
print stock