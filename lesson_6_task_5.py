# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Пишу {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисую {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Выделяю {self.title}')


Pen_1 = Pen('эссе')
Pencil_1 = Pencil('эскиз')
Handle_1 = Handle('заголовки')
Pen_1.draw()
Pencil_1.draw()
Handle_1.draw()
