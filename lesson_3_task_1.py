# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

num_1 = int(input('Введите целое число (делимое): '))
num_2 = int(input('Введите целое число (делитель): '))


def my_func(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Деление на ноль запрещено!')
    else:
        print(f"{num_1} / {num_2} = {result}")


my_func(num_1, num_2)