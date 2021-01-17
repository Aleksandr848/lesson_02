i = 1
product_dict = {}
product_list = []
products = []
while True:
    product_list.clear()
    product_list.append(i)
    product_name = input('Введите название товара: ')
    product_price = input('Введите стоймость товара: ')
    product_sum = input('Введите количество товара: ')
    product_unit = input('Введите единицу измерения: ')
    product_dict.update({'название': product_name, 'цена': product_price, 'количество': product_sum, 'eд': product_unit})
    print(product_dict)
    product_list.append(product_dict)
    product_dict.clear()
    print(product_list)
    product_tuple = tuple(product_list)
    print(product_tuple)
    i += 1
    products.append(product_tuple)
    print(products)

