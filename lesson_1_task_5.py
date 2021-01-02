# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

profit = int(input('Введите прибыль компании: '))
costs = int(input('Введите издержки компании: '))
rent = ((profit - costs) / profit) * 100

if profit > costs:
    print(f'Компания прибыльная. Рентабельность составляет {rent}%')
elif profit < costs:
    print('Компания убыточная.')
else:
    print('Компания вышла в ноль.')

members = int(input('Введите количество сотрудников компании: '))
print(f'Чистая прибыль в расчете не одного сотрудника составляет: {(profit - costs) / members}')
