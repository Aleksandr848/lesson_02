simple_list = input('Введите элементы списка через пробел: ').split()
i = 0
for k in range(int(len(simple_list)/2)):
    simple_list[i], simple_list[i+1] = simple_list[i+1], simple_list[i]
    i += 2
print(simple_list)
