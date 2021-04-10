simple_list = [1, 'dog', 2, True, 3, 'cat', {1, 2, 3, 4}, 4, 'cockroach', 5, False]
i = 1
while simple_list:
    print(f'Тип {i}-го элемента списка {type(simple_list.pop(0))}')
    i += 1
