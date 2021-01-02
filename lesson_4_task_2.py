# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

import random

SIZE = 10
START = 0
STOP = 100
array = [random.randint(START, STOP) for _ in range(SIZE)]
print(array)
result = []

for i in range(1, SIZE):
    if array[i] > array[i - 1]:
        result.append(array[i])

print(result)

# Результат:
# [97, 88, 87, 3, 24, 11, 12, 46, 35, 57]  array
# [24, 12, 46, 57] result
