num = int(input('Введите номер месяца: '))
month_list = ['зима', 'весна', 'лето', 'осень']
if [12, 1, 2].count(num):
    print(month_list[0])
elif [3, 4, 5].count(num):
    print(month_list[1])
elif [6, 7, 8].count(num):
    print(month_list[2])
elif [9, 10, 11].count(num):
    print(month_list[3])
else:
    print('Нет такого месяца!')

num = int(input('Введите номер месяца: '))
month_dict = {
    1 : 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}
print(month_dict[num])
