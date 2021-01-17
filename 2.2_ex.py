simple_list = input('Введите элементы списка через пробел: ').split()
i = 0
copy_list = simple_list.copy()
copy_list.append(1)
while i < len(simple_list):
    if len(simple_list) % 2 == 0:
        simple_list[i], simple_list[i + 1] = simple_list[i + 1], simple_list[i]
    else:
        copy_list[i], copy_list[i + 1] = copy_list[i + 1], copy_list[i]
    i += 2
if len(simple_list) % 2 == 1:
    copy_list.pop(-2)
    print(copy_list)
else:
    print(simple_list)
