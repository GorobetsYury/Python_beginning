# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите положительное целое число: '))
max_ = 0
while number // 10 != 0:
    if number % 10 > max_:
        max_ = number % 10
    number = number // 10
print(f'Максимальное число: {max_}')
