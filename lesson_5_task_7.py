# Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json


with open('lesson_5_task_7.txt', encoding='utf-8') as f:
    arr = f.readlines()

profit = {}
average_profit = {}
average_profit_lst = []
for i in range(len(arr)):
    firm_arr = arr[i].split()
    firm_profit = int(firm_arr[2]) - int(firm_arr[3])
    if firm_profit > 0:
        average_profit_lst.append(firm_profit)
    profit[firm_arr[0]] = firm_profit

sum_ = 0
for _ in average_profit_lst:
    sum_ += _

average_profit_value = sum_ / len(average_profit_lst)
average_profit['average_profit'] = average_profit_value

result = []
result.append(profit)
result.append(average_profit)

with open('lesson_5_task_7.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)

# print(profit)
# {'firm_1': 5000, 'firm_2': 9000, 'firm_3': -4000, 'firm_4': -5000, 'firm_5': 10000, 'firm_6': 20000}
# print(average_profit)
# {'average_profit': 11000.0}
# print(result)
# [{'firm_1': 5000, 'firm_2': 9000, 'firm_3': -4000, 'firm_4': -5000, 'firm_5': 10000, 'firm_6': 20000}, {'average_profit': 11000.0}]
