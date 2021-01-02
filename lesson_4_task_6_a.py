# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle
import sys

# a)
start = int(sys.argv[1])
array = [number for number in range(start, 12)]
for number in cycle(array):
    if number == 11:
        break
    print(number)

# Результат:
# C:\PY_PROJECTS\Foundations\lesson_4>python lesson_4_task_6_a.py 2
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10