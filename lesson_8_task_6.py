# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.

class Store:
    def __init__(self, lst):
        self.lst = lst

    def store_lst(self, obj):  # Метод добавляет объект в список экземпляра класса Store
        self.lst.append(obj.__dict__)
        print(f'На склад добавлен объект {obj}')

    @staticmethod
    def into_store(*args):  #  Метод выводит на печать список словарей с поступившими позициями
        array = [*args]
        result = []
        for k in array:
            result.append(k.__dict__)
        print("На склад поступили следующие позиции: ")
        print(*result, sep="\n")

class MyValidationError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Departments:  #  Класс с департаментами. Завел для удобства распределения техники
    def __init__(self, logistic, finance, marketing):
        self.departments = {logistic: [], finance: [], marketing: []}

    def distribution(self, item, where, how_many):  #  Распределение между департаментами
        self.departments[where].append(item)

        try:  # Прикрутил валидацию через собственный класс ошибок
            if type(how_many) != int:
                raise MyValidationError('Enter number, not a string!')
        except MyValidationError as err:
            print(err)
        else:
            print(f'В депертамент {where} был отправлен {item.manufacturer} в количестве {how_many}шт.')

class OfficeEquipment:
    def __init__(self, price, manufacturer, made_in, quantity):
        self.price = price
        self.manufacturer = manufacturer
        self.made_in = made_in
        self.quantity = quantity

class Printer(OfficeEquipment):
    def __init__(self, price, manufacturer, made_in, quantity, is_coloring):
        super().__init__(price, manufacturer, made_in, quantity)
        self.is_coloring = is_coloring  # Цветной или нет

class Scanner(OfficeEquipment):
    def __init__(self, price, manufacturer, made_in, quantity, resolution):
        super().__init__(price, manufacturer, made_in, quantity)
        self.resolution = resolution  # Разрешение сканнера

class Xerox(OfficeEquipment):
    def __init__(self, price, manufacturer, made_in, quantity, resource):
        super().__init__(price, manufacturer, made_in, quantity)
        self.resource = resource  # Ресурс

# Тестовые данные
MyPrinter = Printer(5500, 'Canon', 2010, 4, True)
MyScanner = Printer(10000, 'Philips', 2018, 2, 'Full HD')
MyXerox = Printer(7500, 'HP', 2015, 1, 150000)
MyStore = Store([])
MyDepartments = Departments('logistic', 'finance', 'marketing')

MyDepartments.distribution(MyXerox, 'finance', 1)
# В депертамент finance был отправлен HP в количестве 1шт.

MyDepartments.distribution(MyXerox, 'finance', "2")
# Enter number, not a string!
