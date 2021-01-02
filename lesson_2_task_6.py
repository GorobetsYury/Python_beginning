# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# Т.к. это задание со звездочкой, решил включить фантизию и пошёл во все тяжкие =) Решил не искать простых путей.

from collections import namedtuple
from collections import defaultdict

result = []

while True:
    Product = namedtuple('Product', 'position_, name_, price_, quantity_, unit_')
    item_ = Product(None, None, None, None, None)
    position = int(input('Введите № товара: '))
    item_ = item_._replace(position_=position)
    name = input('Введите имя товара: ')
    item_ = item_._replace(name_=name)
    price = float(input('Введите цену товара: '))
    item_ = item_._replace(price_=price)
    quantity = int(input('Введите количество товара: '))
    item_ = item_._replace(quantity_=quantity)
    unit = input('Введите ед. изм. товара: ')
    item_ = item_._replace(unit_=unit)
    result.append(item_)

    check = int(input('Если хотите ввести еще товар, то нажмите "1", если хотите закончить "0": '))
    if check == 1:
        pass
    elif check == 0:
        break

print(*result, sep='\n')  # Просто красивый вывод

analytics = defaultdict(list)  # Анализируем

for i in result:
    a = i._asdict()
    for key, val in a.items():
        analytics[key].append(val)
print(analytics)
