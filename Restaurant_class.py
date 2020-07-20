import os
import random
import json
import time



class Restaurant:
	def __init__(self,name,dict1):
			self.f = dict1
			self.name = name
			self.quality = self.f['quality']
			self.age = self.f['age']
			self.totalcustomers = self.f['totalcustomers']
			self.money = float(self.f['money'])
			self.add3 = 0
			self.food = self.f['food']
			self.water = self.f['water']
			self.p_water = self.f['p_water']
			self.p_food = self.f['p_food']
			self.e_water = float(self.f['e_water'])
			self.e_food = float(self.f['e_food'])
			self.expences = float(self.e_water + self.e_food)
			self.a_100_totalcustomers = self.f['a_100_totalcustomers']
			self.a_100_totalmoney = self.f['a_100_totalmoney']
			self.a_20_totalmoney = self.f['a_20_totalmoney']
			self.a_25_space = self.f['a_25_space']
			self.limit = self.f['limit']
			self.p_limit = float(self.f['p_limit'])
			self.saved = 0

	def describe_restaurant(self):
		print(f'Your Restaurant {self.name}\'s infomation')
		print(f'\nMoney                    =  ${"%.2f"%self.money}')
		if self.age == 1:
			print(f'\nAge                      =  {self.age} day')
		else:
			print(f'\nAge                      =  {self.age} days')
		print(f'\nDaily Expences           =  ${"%.2f"%self.expences}')
		print(f'\nMax people in restaurant =  {self.limit}')
		print(f'\nTotal customers          =  {self.totalcustomers}\n')
	def open_restaurant(self):
		print(f'\n{self.name} is open!')
		print('(you can only open once per day)\n')
		print('\n...\n')
		time.sleep(4)
		self.add1 = random.randrange(0,2*self.food + 12)
		if self.add1 > self.limit:
			
			if self.add1 - self.limit == 1:
				print('You have not enough space! 1 person is in queue\n')
			else:
				print(f'You have not enough space! {self.add1 - self.limit} people are in queue\n')
			self.saved = random.randrange(self.food - 1,self.add1 - self.limit)
			if self.saved > 0:
				if self.saved == 1:
					print('Luckly 1 person waited.\n')
				else:
					print(f'Luckly {self.saved} people waited\n')
			self.add1 = self.limit + self.saved
		self.totalcustomers += self.add1
		self.age += 1
		print(f'{self.add1} people entered {self.name} today!')
		if self.a_100_totalcustomers == "False" and self.totalcustomers >= 100:
			print('\nYou have unlocked an achievement: \'Popular Restaurant\' ( Have 100 customers total visit your restaurant )\n')
			self.a_100_totalcustomers = "True"
		for i in range(self.add1):
			self.add2 = float(random.randrange(1,2*self.water + 5))
			self.add3 = float(self.add3)
			self.add3 += self.add2
			self.money += self.add2
		print(f'\nYou earned ${"%.2f"%self.add3} for a total of ${"%.2f"%self.money}')
		self.add3 = 0
		print(f'\n{self.name} is closed\n')
		print(f'\nYou need ${"%.2f"%self.expences} to pay for your expences\n')
		self.money -= self.expences
		if self.money > 0:
			print(f'You now have ${"%.2f"%self.money}')
		if self.a_100_totalmoney == "False" and self.money >= 100:
			print('\nYou have unlocked an achievement: \'Start-up\' ( Have $100 or more )\n')
			self.a_100_totalmoney = "True"
		if self.a_20_totalmoney == "False" and self.money <= 20:
			print('\nYou have unlocked an achievement: \'Failing\' ( Have $20 or less )\n')
			self.a_20_totalmoney = "True"
		self.add1 = 0
		return self.money

	def save(self):
		return {"name":self.name , "quality":self.quality , "age":self.age , "totalcustomers":self.totalcustomers , "money":self.money , "food":self.food , "water":self.water , "p_food":self.p_food , "p_water":self.p_water , "e_water":self.e_water , "e_food":self.e_food , "a_100_totalcustomers":str(self.a_100_totalcustomers) , "a_100_totalmoney":str(self.a_100_totalmoney) , "a_20_totalmoney":str(self.a_20_totalmoney) , "limit":self.limit , "p_limit":self.p_limit , "a_25_space":str(self.a_25_space) }

	def buy(self,item):
		str(item)
		str.lower(item)
		if item == 'water':
			print('\nBetter water brings in more pay per customer\n')
			print(f'Better water costs ${"%.2f"%self.p_water}')
			print(f'\nYou have ${"%.2f"%self.money}')
			item2 = input('\nAre you sure?  ')
			item2 = str(item2)
			item2 = str.lower(item2)
			if item2 == 'yes':
				if self.money < self.p_water:
					print('\nYou do not have enough money')
				else:
					self.money -= self.p_water
					self.water += random.randrange(1,4)
					self.e_water *= 3.5
					self.p_water *= 2.5
					self.quality += 2
					self.expences = float(self.e_water + self.e_food)
					print(f'\nSuccessful!\n{self.name} has {self.quality} quality now! Water now costs ${"%.2f"%self.e_water} per day.\n')

		elif item == 'food':
			print('\nBetter food brings in more customers and has a higher chance of customers staying in the line')
			print(f'\nBetter food costs ${"%.2f"%self.p_food}')
			print(f'\nYou have ${"%.2f"%self.money}')
			item2 = input('\nAre you sure?  ')
			item2 = str(item2)
			item2 = str.lower(item2)
			if item2 == 'yes':
				if self.money < self.p_food:
					print('\nYou do not have enough money')
				else:
					self.money -= self.p_food
					self.food += random.randrange(1,3)
					self.e_food *= 3.5
					self.p_food *= 2.5
					self.quality += 2
					self.expences = float(self.e_water + self.e_food)
					print(f'\nSuccessful!\n{self.name} has {self.quality} quality now! Food now costs ${"%.2f"%self.e_food} per day\n')
		elif item == 'limit':
			print('\nMore space means more customers')
			print(f'\nMore space costs ${"%.2f"%self.p_limit}')
			print(f'\nYou have {"%.2f"%self.money}')
			item2 = input('\nAre you sure?  ')
			item2 = str.lower(item2)
			if item2 == 'yes':
				if self.money < self.p_limit:
					print('\nYou do not have enough money')
				else:
					self.money -= self.p_limit
					self.limit += random.randrange(2,5)
					self.p_limit *= 2.5
					self.quality += 1
					print(f'\nSuccessful!\n{self.name} has {self.quality} quality now!\n')
					if self.a_25_space == "False" and self.limit >= 25:
						print('You have unlocked an achievement: \'Potential\' ( Be able to fit 25 people in your Restaurant )\n')

	def help(self):
		print('\nWhat to type  |  What it means')
		print('Open          -> Opens your restaurant')
		print('Buy           -> Buy water, food and space')
		print('Exit          -> Exits and saves the program')
		print('Info          -> Gives infomation about your Restaurant')
		print('Save          -> Saves your progress')
		print('Reset         -> Resets your progress')
		print('Version       -> Tells what version the program is\n')