# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list = sorted(my_list)
    return my_list[-1] + my_list[-2]


print(my_func(2, 3, -1))
