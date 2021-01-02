# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были
# все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.

with open('lesson_5_task_6.txt', encoding='utf-8') as f:
    array = f.readlines()
    print(array)

result = {}
numbers_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result_val = ''
result_key = None
sum_ = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == ':':
            result_key = array[i][:j]  # Извлёк ключ
        if array[i][j] in numbers_lst:
            result_val = result_val + array[i][j]
        if array[i][j] == '(':
            result_val = result_val + ' '   # Извлёк значения разделенные пробелом
    result_val = result_val.split()
    for num in result_val:
        sum_ = sum_ + int(num)  # Посчитал сумму значений в строке
    result[result_key] = sum_  # Записал в результирующий словарь
    # Обнулил показатели
    result_val = ''
    result_key = None
    sum_ = 0
print(result)
# ['Информатика: 100(л) 50(пр) 20(лаб).\n', 'Физика: 30(л) — 10(лаб)\n', 'Физкультура: — 30(пр) —']
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
