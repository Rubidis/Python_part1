# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


name = input('Введите имя: ')
age = int(input('Введите возраст: '))
city = input('Введите город проживания: ')
def data():
    return f'{name}, {age}, год (а), проживает в городе, {city}'
print(data())

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

x = int(input('Введите 1 число: '))
y = int(input('Введите 2 число: '))
z = int(input('Введите 3 число: '))
def data1():
    return max(x, y, z)
print(data1())


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

str = input('Введите строку 1: ')
str1 = input('Введите строку 2: ')
str2 = input('Введите строку 3: ')

def data3():
    return max(str, str1, str2, key=len)
print(data3())