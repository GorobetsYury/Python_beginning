# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

import random

lst = [random.randint(1, 10) for _ in range(10)]
print(lst)

# Записываю список в файл с пробелами после каждой цифры:
with open('lesson_5_task_5.txt', 'w', encoding='utf-8') as f:
    for i in range(len(lst)):
        f.write(str(lst[i]))
        f.write(' ')

# Считываю всё из файла в result:
with open('lesson_5_task_5.txt', 'r', encoding='utf-8') as f:
    result = f.read()

# Пробегаю по списку с шагом 2, чтобы перескакивать пробелы:
sum_ = 0
for i in range(0, len(result), 2):
    sum_ = sum_ + int(result[i])

print(f'Сумма равна {sum_}')

# Результат
# [1, 9, 9, 1, 6, 2, 3, 2, 6, 7]
# Сумма равна 46
