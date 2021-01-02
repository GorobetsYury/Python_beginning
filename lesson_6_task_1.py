# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
import colorama
from colorama import Fore
colorama.init()

class TrafficLight():

    def __init__(self, color):
        self.__color = color

    def running(self):
        print(self.__color)


traffic_light_1 = TrafficLight('red')
traffic_light_2 = TrafficLight('yellow')
traffic_light_3 = TrafficLight('green')

while True:
    print(Fore.RED + traffic_light_1._TrafficLight__color)
    time.sleep(7)
    print(Fore.YELLOW + traffic_light_2._TrafficLight__color)
    time.sleep(2)
    print(Fore.GREEN + traffic_light_3._TrafficLight__color)
    time.sleep(7)
    print(Fore.YELLOW + traffic_light_2._TrafficLight__color)
    time.sleep(2)










