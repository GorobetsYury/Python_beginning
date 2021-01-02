# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте
# его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


data_1 = int(input('Введите делимое: '))
data_2 = int(input('Введите делитель: '))

try:
    if data_2 == 0:
        raise MyError('MyOwnZeroDivisionError!!!')
except MyError as err:
    print(err)
else:
    result = data_1 / data_2
    print(f'Результат {result}')
