# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
 
class TownCar:
	def __init__(self):
		self.speed = car_speed
		self.color = car_color
		self.name = car_name
		self.is_polise = polise
		
	def go:
		print('Вы начали двигаться')
		
	def stop:
		print('Вы остановились')
		
	def turn:
		if left in turn:
			print('Вы повернули на лево')
			
		if right in turn:
			print('Вы повернули на право')
	
	
class SportCar:
	def __init__(self):
		self.speed = car_speed
		self.color = car_color
		self.name = car_name
		self.is_polise = polise
		
	def go:
		print('Вы начали двигаться')
		
	def stop:
		print('Вы остановились')
		
	def turn:
		if left in turn:
			print('Вы повернули на лево')
			
		if right in turn:
			print('Вы повернули на право')	
	
class WorkCar:
	def __init__(self):
		self.speed = car_speed
		self.color = car_color
		self.name = car_name
		self.is_polise = polise
		
	def go:
		print('Вы начали двигаться')
		
	def stop:
		print('Вы остановились')
		
	def turn:
		if left in turn:
			print('Вы повернули на лево')
			
		if right in turn:
			print('Вы повернули на право')	
	
class PoliceCar:
	def __init__(self):
		self.speed = car_speed
		self.color = car_color
		self.name = car_name
		self.is_polise = polise
		
	def go:
		print('Вы начали двигаться')
		
	def stop:
		print('Вы остановились')
		
	def turn:
		if left in turn:
			print('Вы повернули на лево')
			
		if right in turn:
			print('Вы повернули на право') 
			
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:
	def __init__(self):
		self.speed = car_speed
		self.color = car_color
		self.name = car_name
		self.is_polise = polise
		
	def go:
		print('Вы начали двигаться')
		
	def stop:
		print('Вы остановились')
		
	def turn:
		if left in turn:
			print('Вы повернули на лево')
			
		if right in turn:
			print('Вы повернули на право')	
			
class SportCar(TownCar):
	pass
class WorkCar(TownCar):
	pass
class PoliceCar(TownCar):
	pass
