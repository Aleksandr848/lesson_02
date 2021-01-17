my_list = [7, 5, 3, 3, 2]
rate = int(input('Введите число '))
if rate < my_list[-1]:
    my_list.append(rate)
else:
    for i in my_list:
        if rate >= i:
            b = my_list.index(i)
            my_list.insert(b, rate)
            break
print(my_list)
