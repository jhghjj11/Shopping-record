product = []
while True:
    name = input("Please enter product's name: ")
    if name == 'quit':
        print('Good bye!')
        break
    price = input('Please enter the price: ')
    if price == 'quit':
        print('Good bye!')
        break
    #p = []
    #p.append(name)
    #p.append(price)
    #p = [name, price]
    #product.append(p)
    product.append([name, price])
print('Products storage: ', product)

for things in product :
    print(things[0], 'has a price at', things[1])
