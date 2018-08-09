x = 1
y = 3
z = y + 5
q = z + x + y

print(z)
print(q)

chi = int(input('Введите число: '))
print(q + chi)

chi1 = int(input('Введите число: '))
print(2 + chi1)

age = int(input('Сколько вам лет: ')) # В начале сделал ошибку, забыл про int, вводим же возраст
if age < 18:
    print('"Извините, пользование данным ресурсом только с 18 лет"')
elif age >= 18:
    print('"Доступ разрешен"')