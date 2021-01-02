# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('lesson_5_task_3.txt', encoding='utf-8') as f:
    array = f.readlines()

print(array)

losers = []
sum_ = 0
for person in array:
    result = person.split()
    if int(result[1]) < 20000:
        losers.append(result[0])
    sum_ = sum_ + int(result[1])

average_salary = round(sum_ / len(array))
print(f'Меньше 20 тыс. получают {losers}')
print(f'Средняя зарплата - {average_salary}')
