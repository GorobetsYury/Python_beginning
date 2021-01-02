# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Store:
    pass

class OfficeEquipment:
    def __init__(self, price, manufacturer, made_in):
        self.price = price
        self.manufacturer = manufacturer
        self.made_in = made_in

class Printer(OfficeEquipment):
    def __init__(self, price, manufacturer, made_in, is_coloring):
        super().__init__(price, manufacturer, made_in)
        self.is_coloring = is_coloring  # Цветной или нет

class Scanner(OfficeEquipment):
    def __init__(self, price, manufacturer, made_in, resolution):
        super().__init__(price, manufacturer, made_in)
        self.resolution = resolution  # Разрешение сканнера

class Xerox(OfficeEquipment):
    def __init__(self, price, manufacturer, made_in, resource):
        super().__init__(price, manufacturer, made_in)
        self.resource = resource  # Ресурс
