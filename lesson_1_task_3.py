#  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
#  пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число n: '))
nn = n*10 + n
nnn = n*100 + nn
sum_ = n + nn + nnn
print(f'Сумма чисел n + nn + nnn равна: {n} + {nn} + {nnn} = {sum_}')
