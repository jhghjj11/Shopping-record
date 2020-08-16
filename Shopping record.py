product = []

with open('products.csv', 'r', encoding = 'utf-8') as d:
    for line in d:
        if '第一, 第二' in line:
            continue
        name, price = line.strip().split(',')
        product.append([name, price])
        #name = s[0]
        #price = s[1]
    print(product)

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

with open('products.csv', 'w', encoding = 'utf-8') as f :
    f.write('第一, 第二 \n')
    for p in product:
        f.write(p[0]  + ',' + str(p[1]) + '\n')
