# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

# Способ №1
array = [number for number in range(20, 241) if number % 20 == 0 or number % 21 == 0]
print(array)

# Способ №2
result = filter(lambda number: number % 20 == 0 or number % 21 == 0, range(20, 241))
print(list(result))
