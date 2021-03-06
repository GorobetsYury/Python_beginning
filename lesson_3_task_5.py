# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
# вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

total = []
while True:
    list_input = input('Введите числа через пробел (q - выход): ').split()
    for _ in list_input:
        if _ in {" ", "q"}:
            pass
        else:
            total.append(int(_))
    print(f"Сумма введенных Вами элементов равна {sum(total)}")
    if "q" in list_input:
        break
print("Конец!")
