# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
number = int(input('Введите любое натуральное число: '))
for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        break
    if number <= my_list[-1]:
        my_list.append(number)
        break
print(my_list)
