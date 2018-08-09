print('Здравствуйте, введите следующие данные: ')
name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))

if age < 29 or 50 < weight < 120:
    print(name, surname,',', age,'год',',', 'вес', weight, '- хорошее состояние' )
    
elif 30 <= age <= 39 or 49 >= weight >= 119:
    print(name, surname, ',', age, 'год', ',', 'вес', weight, '- следует занятся собой')

elif age >= 40 or 50 >= weight >= 120:
    print(name, surname, ',', age, 'год', ',', 'вес', weight, '- следует обратится к врачу')
