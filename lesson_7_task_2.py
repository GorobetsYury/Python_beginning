# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v=10, h=10):
        self.v = v
        self.h = h

    @abstractmethod
    def result_coat(self):
        return self.v/6.5 + 0.5

    @abstractmethod
    def result_costume(self):
        return (2 * self.h + 0.3)


class Coat(Clothes):
    def result_coat(self):
        return self.v/6.5 + 0.5

    def result_costume(self):
        pass


class Costume(Clothes):
    def result_costume(self):
        return (2 * self.h + 0.3)

    def result_coat(self):
        pass


coat_1 = Coat()
costume_1 = Costume()
print(coat_1.result_coat())
print(costume_1.result_costume())
print(round(coat_1.result_coat() + costume_1.result_costume(), 2))
