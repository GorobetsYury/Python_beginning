# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

array = [number for number in range(100, 1001) if number % 2 == 0]

def reduce_mult(first, second):
    return first * second

def reduce_sum(first, second):
    return first + second

print(f'Массив:{array}')
print(f'Сумма: {reduce(reduce_sum, array)}')
print(f'Произведение: {reduce(reduce_mult, array)}')
