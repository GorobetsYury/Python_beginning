# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexObject:
    def __init__(self, a, b):
        self.a = a #  действительная часть
        self.b = b #  мнимая часть

    def show_complex(self): # рассматриваю только случай, где и 'a' и 'b' != 0
        if self.b > 0:
            print(f'{self.a}+{self.b}i')
        if self.b < 0:
            print(f'{self.a}{self.b}i')

    # z1⋅z2=(a1+b1i)⋅(a2+b2i)=(a1⋅a2−b1⋅b2)+(a1⋅b2+a2⋅b1)i
    def __mul__(self, other):
        if (self.a*other.b + other.a*self.b) > 0:
            return f'{(self.a*other.a - self.b*other.b)}+{(self.a*other.b + other.a*self.b)}i'
        elif (self.a*other.b + other.a*self.b) < 0:
            return f'{(self.a*other.a - self.b*other.b)}{(self.a*other.b + other.a*self.b)}i'

    #z1+z2=(a1+b1)+(a2+b2)=(a1+a2)+(b1+b2)i
    def __add__(self, other):
        if self.b+other.b > 0:
            return f'{self.a+other.a}+{self.b+other.b}i'
        elif self.b+other.b < 0:
            return f'{self.a+other.a}{self.b+other.b}i'


co_1 = ComplexObject(3, 1)
co_2 = ComplexObject(2, -3)
co_1.show_complex()  # 3+1i
co_2.show_complex()  # 2-3i
print(co_1 * co_2)  # 9-7i
print(co_1 + co_2)  # 5-2i
