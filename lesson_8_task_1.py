# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
# виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
# с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def check_date(obj):
        data = obj.date.split('-')
        new_data = []
        for item in data:
            new_data.append(int(item))
        if new_data[1] == 2 and new_data[0] > 28:  # не стал учитывать високосный год
            print('Дата некорректна')
        elif 1 <= new_data[0] <= 31:
            if 1 <= new_data[1] <= 12:
                if 1 <= new_data[2] <= 9999:
                    print('Дата верна')


    @classmethod
    def str_to_int(cls, data):
        data = data.split('-')
        new_data = []
        for item in data:
            new_data.append(int(item))
        print(f'Число {new_data[0]} (тип {type(new_data[0])}), '
               f'Месяц {new_data[1]} (тип {type(new_data[1])}), '
               f'Год {new_data[2]} (тип {type(new_data[2])})')

my_date = Date('18-11-1990')
my_date_2 = Date('30-02-2020')
Date.str_to_int(my_date.date)
# Результат:
# Число 18 (тип <class 'int'>), Месяц 11 (тип <class 'int'>), Год 1990 (тип <class 'int'>)

Date.check_date(my_date)  # Дата верна
Date.check_date(my_date_2)  # Дата некорректна
