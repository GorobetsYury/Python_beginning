# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle
import sys

# b)
num_of_repeat = int(sys.argv[1])
array = [1, 2, 3, 4, 5]
check_list = []
for num in cycle(array):
    print(num)
    if num == array[-1]:
        check_list.append(num)
        if check_list.count(num) == num_of_repeat:
            break
print(f'Цикл повторился {num_of_repeat} раз(-а)')

# Результат
# C:\PY_PROJECTS\Foundations\lesson_4>python lesson_4_task_6_b.py 2
# 1
# 2
# 3
# 4
# 5
# 1
# 2
# 3
# 4
# 5
# Цикл повторился 2 раз(-а)
