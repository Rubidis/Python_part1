_author_ = ('Волков Николай Дмитриевич')

import math
print('Задача №1')
po = int(input('Введите число от 1 до 9: '))

while po < 1 or po > 9:  # Сделал так как по условиям задачи должен быть > 0 и < 10 а не <= или >=.
    print('Введите заного! ')
    po = int(input('Введите число от 1 до 9: '))
print(po ** 2)

print('Задача №2')

po1 = int(input('Введите первое число: '))
po2 = int(input('Введите второе число: '))

print(po2, po1)


print('Задача №3')
# Честно посмотрел решение в интернете, но после того как нашел формулу понял почему сделано так.

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c;
print("Дискриминант D = %.2f" % discr)
if discr > 0:

    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")