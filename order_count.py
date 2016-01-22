def item_order(order):
    num_salad = 0
    num_burger = 0
    num_water = 0
    items = order.split(' ')
    for item in items:
        if item == 'salad':
            num_salad += 1
        elif item == 'hamburger':
            num_burger += 1
        elif item == 'water':
            num_water += 1
    return 'salad:'+str(num_salad)+' hamburger:'+str(num_burger)+' water:'+str(num_water)

if __name__ == '__main__':
    print item_order('water hamburger salad salad')
