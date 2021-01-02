# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

var_1 = 'hello'
print(var_1)
print(type(var_1))

var_2 = 123
print(var_2)
print(type(var_2))

var_3 = int(input('Введите любое число: '))
print(var_3)
print(var_2 == var_3) # True or False
print(type(var_2 == var_3))

var_4 = input('Введите что-нибудь: ')
print(f'Вы ввели: {var_4}')
