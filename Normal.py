# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

	def __init__(self):
		self.name = name
		self.health = health
		self.damage = damage
		self.armor = armor
	
		
	def generate_person_by_name(name, health=100, damage=50, armor=0.7):
    return {'name': name, 'health': health, 'damage': damage, 'armor': armor}
	
	def write_person_to_file(person):
    with open(person['name'], 'w', encoding='UTF-8') as f:
        for key, value in person.items():
            f.write('{} {}\n'.format(key, value))



	def get_person_by_filename(filename):
    	person = {}
    		with open(filename, encoding='UTF-8') as f:
        		for line in f:
        			 key, value = line.split()
            
            	if key == 'armor':
                	value = float(value)
            	elif key != 'name':
                	value = int(value)
            
            	person[key] = value

    return person
    
	def __init__(self):
		self.calculate_damage = fight_damage
		self.attack = attack_person
		
		
	def calculate_damage(damage, armor):
    	return damage // armor

	def attack(who_attack, who_defend):
    	damage = calculate_damage(who_attack['damage'], who_defend['armor'])
    	who_defend['health'] -= damage
    	print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack['name'], who_defend['name'], damage,
                                                                    who_defend['health']))    
                                                                    
class Player(Person):
	pass

class Enemy(Person):
	pass

class Fight:
	def start_game():
    # получаем наши структуры, через вышеописанную функцию
    player = get_person_by_filename(player_name)
    enemy = get_person_by_filename(enemy_name)

    # Запоминаем кто последний атаковал
    last_attacker = player
    while player['health'] > 0 and enemy['health'] > 0:
        if last_attacker == player:
            attack(enemy, player)
            last_attacker = enemy
        else:
            attack(player, enemy)
            last_attacker = player

    if player['health'] > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')


Fight.start_game()