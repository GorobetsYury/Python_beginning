# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('lesson_5_task_2.txt', encoding='utf-8') as f:
    array = f.readlines()

print(array)
count = 0
for i in range(len(array)):
    print(f'количество слов в {i + 1} строке - {len(array[i].split())}')
    count += 1

print(f'В файле {count} строк(-и)')
