#  Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
#  на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
#  и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую
#  структуру, например словарь.

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

class Departments:  #  Класс с департаментами. Завел для удобства распределения техники
    def __init__(self, logistic, finance, marketing):
        self.departments = {logistic: [], finance: [], marketing: []}

    def distribution(self, item, where, how_many):  #  Распределение между департаментами
        self.departments[where].append(item)
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

MyStore.into_store(MyPrinter, MyScanner, MyXerox)
# На склад поступили следующие позиции:
# {'price': 5500, 'manufacturer': 'Canon', 'made_in': 2010, 'quantity': 4, 'is_coloring': True}
# {'price': 10000, 'manufacturer': 'Philips', 'made_in': 2018, 'quantity': 2, 'is_coloring': 'Full HD'}
# {'price': 7500, 'manufacturer': 'HP', 'made_in': 2015, 'quantity': 1, 'is_coloring': 150000}

MyStore.store_lst(MyPrinter)
print(MyStore.lst)
# На склад добавлен объект <__main__.Printer object at 0x000001FC55004B80>
# [{'price': 5500, 'manufacturer': 'Canon', 'made_in': 2010, 'quantity': 4, 'is_coloring': True}]

MyDepartments.distribution(MyXerox, 'finance', 1)
# В депертамент finance был отправлен HP в количестве 1шт.
