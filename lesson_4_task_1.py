# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

working_hours = sys.argv[1]
rate_per_hour = sys.argv[2]
premium = sys.argv[3]


def my_cash(a, b, c):
    a, b, c = int(a), int(b), int(c)
    salary = (a * b) + c
    return salary


print(f'Заработная плата cотрудника с введенными параметрами равна: {my_cash(working_hours, rate_per_hour, premium)}')

# Результат
# C:\PY_PROJECTS\Foundations\lesson_4>python lesson_4_task_1.py 2 3 4
# Заработная плата зотрудника с введенными параметрами равна: 10
