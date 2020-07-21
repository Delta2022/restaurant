
# Released on Friday, July 15 2020
# Runnable on IDLE, Thonny and VS code
# To run on Thonny, replace all tabs with 4 spaces
# Using Python 3.8.4
# Any problems can be emailed  to zi.azzr227@gmail.com
# Copyright © 2020 Alvin Ran 
# July 20, 2020

import random
import time
import json
import os
from Restaurant_class import Restaurant

VERSION = 'Snapshot 1.2.8.2 '

absPath = os.path.abspath(__file__)
currentPath = os.path.dirname(__file__)
commandStr = 'cd '+currentPath
os.system(commandStr)
filename = absPath.replace('.py' , '.json')
if not os.path.exists(filename):
	with open(filename , 'w') as f2:
		json.dump({"name": "", "quality": 1, "age": 0, "totalcustomers": 0, "money": 50, "food": 1, "water": 1, "p_food": 100, "p_water": 75, "e_water": 2, "e_food": 2, "a_100_totalcustomers": "False", "a_100_totalmoney": "False", "a_20_totalmoney": "False" , "limit":10 , "p_limit":75 , "a_25_space":"False"}, f2)

with open(filename , 'r') as f1:
	value = json.load(f1)
if value['name'] == "":
	a227 = input('Welcome! Please enter your restaurant\'s name:  ')

	aiyo = Restaurant(str(a227),value)
	aiyo.describe_restaurant()
	print('Start buy typing \'open\' below, when you get $75 buy water (type \'buy\' then \'water\'). Type \'info\' to see how you are doing ( Do this after typing open for the first time ). Type \'exit\' to exit\n')

else:
	print(f"\nWelcome back to your restaurant: {value['name']}\n")
	aiyo = Restaurant(value['name'],value)
	aiyo.describe_restaurant()
flag = True

flag1 = False
while flag:
		next1 = input('What do you want to do?  ')
		next1 = str.lower(next1)
		
		if next1 == 'open':
			hi = aiyo.open_restaurant()
			if hi <= 0:
				print('You are now Bankrupt')
				with open(filename, 'w') as f5:
					json.dump({"name": "", "quality": 1, "age": 0, "totalcustomers": 0, "money": 50, "food": 1, "water": 1, "p_food": 100, "p_water": 75, "e_water": 2, "e_food": 2, "a_100_totalcustomers": "False", "a_100_totalmoney": "False", "a_20_totalmoney": "False" , "limit":10 , "p_limit":75 , "a_25_space":"False"}, f5)
					flag = False
					flag1 = True
		elif next1 == 'exit':
			flag = False
		elif next1 == 'info':
			aiyo.describe_restaurant()
		elif next1 == 'buy':
			next2 = input('What do you want to buy?  ')
			next2 = str.lower(next2)
			if next2 == 'water':
				aiyo.buy('water')
			elif next2 == 'food':
				aiyo.buy('food')
			elif next2 == ('space'):
				aiyo.buy('limit')
			elif next2 == 'prices':
				aiyo.buy('prices')
		

			else:
				print('what?')
		elif next1 == 'reset':
			with open(filename, 'w') as f2:
				next3 = input('Are you sure?  ')
				next3 = str.lower(next3)
				if next3 == 'yes':
					json.dump({"name": "", "quality": 1, "age": 0, "totalcustomers": 0, "money": 50, "food": 1, "water": 1, "p_food": 100, "p_water": 75, "e_water": 2, "e_food": 2, "a_100_totalcustomers": "False", "a_100_totalmoney": "False", "a_20_totalmoney": "False" , "limit":10 , "p_limit":75 , "a_25_space":"False"}, f2)
					flag = False
					flag1 = True
				else:
					print('\nReset Cancelled\n')
		elif next1 == 'save':
			a = aiyo.save()
			with open(filename , 'w') as f11:
				json.dump(a , f11)
			('\nProgress saved\n')
		elif next1 == 'version':
			print(f'\nRestaurant is running on {VERSION}\n')
		elif next1 == 'help' or next1 == 'h':
			aiyo.help()

		else:
				print('what?')
if flag1 == False:
	a = aiyo.save()
	with open(filename , 'w') as f11:
		json.dump(a , f11)
print('The end')