# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

my_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',
}

month = int(input('Введите номер месяца: '))
print(f'Это будет время года - {my_dict[month]}')

my_list = [None, 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer',
           'autumn', 'autumn', 'autumn', 'winter']
month = int(input('Введите номер месяца: '))
print(f'Это будет время года - {my_list[month]}')
