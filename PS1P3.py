def item_order(order):
    items = order.split(' ')
    salad = 0
    water = 0
    hamburger = 0
    for i in items:
        if i == 'salad':
            salad += 1
        elif i == 'hamburger':
            hamburger += 1
        elif i == 'water':
            water += 1
    return "salad:" + str(salad) + " hamburger:" + str(hamburger) + " water:" + str(water)

print item_order("salad water hamburger salad hamburger")
print item_order("hamburger water hamburger")
