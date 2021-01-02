# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(**kwargs):
    print(kwargs)  # либо словарь
    print(*kwargs.values())  # либо значения


my_func(name="Yury", surname="Gorobets", born_in=1990, city="Moscow",
        email="mail@mail.ru", phone="8903xxxxxx")

# Результаты:
# {'name': 'Yury', 'surname': 'Gorobets', 'born_in': 1990, 'city': 'Moscow',
# 'email': 'mail@mail.ru', 'phone': '8903xxxxxx'}
# Yury Gorobets 1990 Moscow mail@mail.ru 8903xxx
