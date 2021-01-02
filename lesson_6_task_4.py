# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go-go-go!')

    def stop(self):
        print('STOOOOP!')

    def turn(self, direction):
        print(f'A car turn {direction}')

    def show_speed(self):
        print(f'Скорость машины равна {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Предупреждение! Скорость машины превышает 60 и равна {self.speed}!')
        else:
            f'Скорость машины равна {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Предупреждение! Скорость машины превышает 60 и равна {self.speed}!')
        else:
            f'Скорость машины равна {self.speed}'


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


TownCar_1 = TownCar(79, 'Red', 'Lexus')
print(TownCar_1.speed)
print(TownCar_1.color)
print(TownCar_1.name)
print(TownCar_1.is_police)
TownCar_1.go()
TownCar_1.stop()
TownCar_1.turn('right')
TownCar_1.show_speed()
print('***' * 5)
SportCar_1 = SportCar(120, 'Blue', 'Ferrari')
print(SportCar_1.speed)
print(SportCar_1.color)
print(SportCar_1.name)
print(SportCar_1.is_police)
SportCar_1.go()
SportCar_1.stop()
SportCar_1.turn('right')
SportCar_1.show_speed()
print('***' * 5)
WorkCar_1 = WorkCar(39, 'Green', 'Ford')
print(WorkCar_1.speed)
print(WorkCar_1.color)
print(WorkCar_1.name)
print(WorkCar_1.is_police)
WorkCar_1.go()
WorkCar_1.stop()
WorkCar_1.turn('left')
WorkCar_1.show_speed()
print('***' * 5)
PoliceCar_1 = PoliceCar(100, 'While-Blue', 'Skoda')
print(PoliceCar_1.speed)
print(PoliceCar_1.color)
print(PoliceCar_1.name)
print(PoliceCar_1.is_police)
PoliceCar_1.go()
PoliceCar_1.stop()
PoliceCar_1.turn('left')
PoliceCar_1.show_speed()
print('***' * 5)