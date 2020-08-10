product = []
while True:
    name = input("Please enter product's name: ")
    if name == 'quit':
        print('Good bye!')
        break
    price = input('Please enter the price: ')
    price = int(price)
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

with open('products.csv', 'w') as f :
    for p in product:
        f.write(p[0]  + ',' + str(p[1]) + '\n')
