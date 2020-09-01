""" Contains the class for the Model """
import random
from json import load, dump
from datetime import date
from os import path

VERSION = 'Version 1.3.0'
VERSION_DATE = 'August 31 2020'
DATE = date.today().day
JSON_VAR = {
                "name": "",
                "quality": 1,
                "age": {"year": 2008, "month": 2, "day": 27, },
                "totalcustomers": 0,
                "money": 50,
                "food": 1,
                "water": 1,
                "p_food": 100,
                "p_water": 75,
                "e_water": 2,
                "e_food": 2,
                "a_100_totalcustomers": "False",
                "a_100_totalmoney": "False",
                "a_20_totalmoney": "False",
                "a_1000_totalmoney": "False",
                "limit": 10,
                "p_limit": 75,
                "a_25_space": "False",
                "date": DATE + 1,
                "streak": 0,
                "o_day": {
                    "year": date.today().year, "month": date.today(
                    ).month, "day": date.today().day, "dow": date.today().
                                                      weekday()
                }
                }


class Model:
    """ The Model class of the Restaurant """
    def __init__(self, name=""):
        """ JSON reading and all variables defined here """
        self.json_file = path.abspath(__file__)
        self.json_file = self.json_file.replace('.py', '.json')
        self.json_file = self.json_file.replace('_model', '')
        self.json_file = self.json_file.replace('R', '.R')
        try:
            with open(self.json_file) as temp_file:  # Loads the var from
                # .json file
                self.file = load(temp_file)
                self.save = True  # Tells the rest of the program to save
        except FileNotFoundError:
            with open(self.json_file, 'w') as f1:
                dump(JSON_VAR, f1)
            with open(self.json_file) as f1:
                self.file = load(f1)

        # Defining variables for the program
        self.name = name
        self.quality = self.file['quality']
        self.age = self.file['age']
        if self.age["year"] == 2008:
            self.age = {"year": date.today().year, "month": date.today().month,
                        "day": date.today().day, "dow": date.today().weekday()}
        self.totalcustomers = self.file['totalcustomers']
        self.money = float(self.file['money'])
        self.add3 = 0
        self.food = self.file['food']
        self.water = self.file['water']
        self.p_water = self.file['p_water']
        self.p_food = self.file['p_food']
        self.e_water = float(self.file['e_water'])
        self.e_food = float(self.file['e_food'])
        self.expenses = float(self.e_water + self.e_food)
        self.a_100_totalcustomers = self.file['a_100_totalcustomers']
        self.a_100_totalmoney = self.file['a_100_totalmoney']
        self.a_20_totalmoney = self.file['a_20_totalmoney']
        self.a_25_space = self.file['a_25_space']
        self.a_1000_totalmoney = self.file['a_1000_totalmoney']
        self.limit = self.file['limit']
        self.p_limit = float(self.file['p_limit'])
        self.saved = 0
        self.gst = 0
        self.add1 = 0
        self.add2 = 0
        self.add3 = 0
        self.o_day = self.file['o_day']
        self.day_names = ["Monday", "Tuesday", "Wednesday", "Thursday",
                          "Friday",
                          "Saturday", "Sunday"]
        self.month_names = ['THING', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                            'Jul',
                            'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.streak = self.file['streak']
        if self.file['date'] == DATE:
            self.money += self.streak * 10
            self.streak += 1
        elif self.file['date'] < DATE:
            self.streak = 0

    def r_open(self):
        """ Opens the Restaurant """
        ans = ''
        ans1 = ''
        if not self.age['dow'] in (1, 2):
            ans1 += str(f'\n\n{self.name} is open!')
            ans1 += str('\n(you can only open once per day)\n')
            ans1 += str('\n\n...\n')
            self.add1 = random.randrange(0, 2*self.food + 12)
            if self.add1 > self.limit:

                if self.add1 - self.limit == 1:
                    ans += str('\nYou have not enough space! 1 person is in '
                               'queue')
                else:
                    ans += str(f'\nYou have not enough space!'
                               f' {self.add1 - self.limit} people are in '
                               f'queue')
                if self.food - 6 < self.add1 - self.limit:
                    if self.food - 1 != self.add1 - self.limit - 1:
                        self.saved = random.randrange(self.food - 1,
                                                      self.add1 -
                                                      self.limit-1, 1)
                    else:
                        self.saved = 0
                else:
                    self.saved = random.randrange(self.add1 - self.limit - 5,
                                                  self.add1 - self.limit-1, 1)
                if self.saved > 0:
                    if self.saved == 1:
                        ans += str('\n1 person waited but'
                                   f' {self.add1 - self.limit - self.saved} '
                                   f'people'
                                   ' left\n')
                    else:
                        ans += str(f'\n{self.saved} people waited but '
                                   f'{self.add1 - self.limit - self.saved} '
                                   f'left\n')
                else:
                    ans += str('\nEverybody left\n')
                self.add1 = self.limit + self.saved
            self.totalcustomers += self.add1
            self.age["day"] += 1
            self.age["dow"] += 1
            if self.age["day"] > 30 and self.age['month'] in (4, 6, 9, 11):
                self.age["month"] += 1
                self.age["day"] = 1
            elif self.age["day"] > 31 and self.age["month"] in (1, 3, 5, 7, 8,
                                                                10, 12):
                self.age["month"] += 1
                self.age["day"] = 1
            elif self.age["day"] > 28 and self.age["month"] == 2:
                self.age["month"] += 1

            if self.age["month"] > 12:
                self.age["year"] += 1
                self.age["month"] = 1

            if self.age["dow"] > 6:
                self.age["dow"] = 0

            ans += str(f'\n{self.add1} people entered {self.name} today!')
            if self.a_100_totalcustomers == "False" and self.totalcustomers \
                    >= 100:
                ans += str('\n\nYou have unlocked an achievement: '
                           '\'Popular Restaurant\' '
                           '( Have 100 customers total visit your restaurant'
                           ' )\n')
                self.a_100_totalcustomers = "True"
            for i in range(self.add1):
                self.add2 = float(random.randrange(1, 2*self.water + 5))
                self.add3 = float(self.add3)
                self.gst = self.add2 * 0.05
                self.add2 = round(1.05*self.add2, 2)
                self.add3 += self.add2
                self.money += self.add2
            ans += str(f'\n\nYou earned ${"%.2f"%self.add3} + GST for a '
                       f'total of'
                       f' ${"%.2f"%self.money}\n')
            self.add3 = 0

            ans += str(f'\nYou need ${"%.2f"%self.expenses} to pay for your '
                       'expenses\n')
            self.money -= self.expenses
            if self.money > 0:
                ans += str(f'\nYou now have ${"%.2f"%self.money}\n')

            if self.a_100_totalmoney == "False" and self.money >= 100:
                ans += str('\n\nYou have unlocked an achievement: \'Start-up\''
                           ' ( Have $100 or more )\n')
                self.a_100_totalmoney = "True"
            if self.a_20_totalmoney == "False" and self.money <= 20:
                ans += str('\n\nYou have unlocked an achievement: \'Failing\''
                           ' ( Have $20 or less )\n')
                self.a_20_totalmoney = "True"
            if self.a_1000_totalmoney == "False" and self.money >= 1000:
                ans += str('\n\nYou have unlocked an achievement: \'Rich\''
                           ' ( Have $1000 or more)\n')
                self.a_1000_totalmoney = "True"

            self.add1 = 0
            ans += str(f'\n{self.name} is closed\n')

            list1 = [ans1, ans]

        else:
            list1 = ['Today is a break day', f'{self.name} is closed']
            self.age["day"] += 1
            self.age["dow"] += 1
            if self.age["day"] > 30 and self.age['month'] in (4, 6, 9, 11):
                self.age["month"] += 1
                self.age["day"] = 1
            elif self.age["day"] > 31 and self.age["month"] in (1, 3, 5, 7, 8,
                                                                10, 12):
                self.age["month"] += 1
                self.age["day"] = 1
            elif self.age["day"] > 28 and self.age["month"] == 2:
                self.age["month"] += 1
                self.age["day"] = 1

            if self.age["month"] > 12:
                self.age["year"] += 1
                self.age["month"] = 1
        return list1

    def r_save(self):
        """ Saves the info """
        if self.save:
            with open(self.json_file, 'w') as temp_file:
                dump({
                    "name": self.name,
                    "quality": self.quality,
                    "age": self.age,
                    "totalcustomers": self.totalcustomers,
                    "money": round(self.money, 2),
                    "food": self.food,
                    "water": self.water,
                    "p_food": self.p_food,
                    "p_water": self.p_water,
                    "e_water": self.e_water,
                    "e_food": self.e_food,
                    "a_100_totalcustomers": str(self.a_100_totalcustomers),
                    "a_100_totalmoney": str(self.a_100_totalmoney),
                    "a_20_totalmoney": str(self.a_20_totalmoney),
                    "a_1000_totalmoney": str(self.a_1000_totalmoney),
                    "limit": self.limit,
                    "p_limit": self.p_limit,
                    "a_25_space": str(self.a_25_space),
                    "date": DATE + 1,
                    "streak": self.streak,
                    "o_day": self.o_day
                    }, temp_file)
            return '\nProgress Saved\n'
        else:
            return '\nSave Unsuccessful (ED #1)\n'

    def r_buy(self, item):
        """ Opens the shop menu """
        ans = ''
        str(item)
        str.lower(item)
        if item == 'water':
            ans += str('\nBetter water brings in more pay per customer\n')
            ans += str(f'Better water costs ${"%.2f"%self.p_water}')
            ans += str(f'\nYou have ${"%.2f"%self.money}')
            item2 = 'yes'
            item2 = str(item2)
            item2 = str.lower(item2)
            if item2 == 'yes':
                if self.money < self.p_water:
                    ans += str('\nYou do not have enough money')
                else:
                    self.money -= self.p_water
                    self.water += random.randrange(1, 4)
                    self.e_water *= 3.5
                    self.p_water *= 2.5
                    self.quality += 2
                    self.expenses = float(self.e_water + self.e_food)
                    ans += str(f'\nSuccessful!\n{self.name} has {self.quality}'
                               f' quality now! Water now costs'
                               f' ${"%.2f"%self.e_water} per day.\n')
            else:
                ans += str('\nCancelled\n')

        elif item == 'food':
            ans += str('\nBetter food brings in more customers and has a'
                       ' higher chance of customers staying in the line')
            ans += str(f'\nBetter food costs ${"%.2f"%self.p_food}')
            ans += str(f'\nYou have ${"%.2f"%self.money}')
            item2 = 'yes'
            item2 = str(item2)
            item2 = str.lower(item2)
            if item2 == 'yes':
                if self.money < self.p_food:
                    ans += str('\nYou do not have enough money')
                else:
                    self.money -= self.p_food
                    self.food += random.randrange(1, 3)
                    self.e_food *= 3.5
                    self.p_food *= 2.5
                    self.quality += 2
                    self.expenses = float(self.e_water + self.e_food)
                    ans += str(f'\nSuccessful!\n{self.name} has'
                               f' {self.quality} quality now! Food now costs'
                               f' ${"%.2f"%self.e_food} per day\n')
            else:
                ans += str('\nCancelled\n')

        elif item == 'prices':
            ans += str(f'\nWater costs ${"%.2f"%self.p_water}')
            ans += str(f'\nFood costs ${"%.2f"%self.p_food}')
            ans += str(f'\nMore space costs ${"%.2f"%self.p_limit}\n')
            ans += str(f'\nYou have ${"%.2f"%self.money}\n')

        elif item == 'limit':
            ans += str('\nMore space means more customers')
            ans += str(f'\nMore space costs ${"%.2f"%self.p_limit}')
            ans += str(f'\nYou have {"%.2f"%self.money}')
            item2 = 'yes'
            item2 = str.lower(item2)
            if item2 == 'yes':
                if self.money < self.p_limit:
                    ans += str('\nYou do not have enough money')
                else:
                    self.money -= self.p_limit
                    self.limit += random.randrange(2, 5)
                    self.p_limit *= 2.5
                    self.quality += 1
                    ans += str(f'\nSuccessful!\n{self.name} has'
                               f' {self.quality} quality now!\n')
                    if self.a_25_space == "False" and self.limit >= 25:
                        ans += str('You have unlocked an achievement:'
                                   ' \'Potential\' ( Be able to fit 25 '
                                   'people in your Restaurant )\n')
            else:
                ans += str('\nCancelled\n')

        return ans

    def r_describe(self):
        """ Describes your restaurant """
        ans = ''
        # self.age["dow"] = date.today().weekday()
        ans += str(f'\nYour Restaurant {self.name}\'s information:\n')
        ans += str(f'\nDate                     =  '
                   f'{self.day_names[self.age["dow"]]}, '
                   f'{self.month_names[self.age["month"]]} '
                   f'{self.age["day"]}, {self.age["year"]}')
        ans += str(f'\nOpening Date             =  '
                   f'{self.day_names[self.o_day["dow"]]}, '
                   f'{self.month_names[self.o_day["month"]]} '
                   f'{self.o_day["day"]}, {self.age["year"]}')
        ans += str(f'\nDaily Expenses           =  ${"%.2f"%self.expenses}')
        ans += str(f'\nMax customer capacity    =  {self.limit}')
        ans += str(f'\nTotal customers served   =  {self.totalcustomers}')
        ans += str(f'\nMoney                    =  ${"%.2f"%self.money}\n')
        return ans

    def rename(self, name1):
        """ Renames the restaurant """
        ans = ''
        if name1 == self.name:
            ans += str('\nName not changed\n')
        else:
            ans += str('\nName change successful!\n')
            ans += str(f'Your restaurant\'s name is now {name1}\n')
            self.name = name1
        return ans

    def help(self):
        """ Help """
        ans = ''
        ans += str('\n\nWhat to type  |  What it means')
        ans += str('\nOpen          -> Opens your restaurant')
        ans += str('\nShop          -> Opens the Shop Menu')
        ans += str('\nExit          -> Exits and saves the program. If used'
                   ' in the Shop Menu, Exits the Shop Menu')
        ans += str('\nInfo          -> Gives information about your '
                   ' Restaurant')
        ans += str('\nSave          -> Saves your progress')
        ans += str('\nReset         -> Resets your progress')
        ans += str('\nAbout         -> Shows Version and other data'
                   ' about program')
        ans += str('\nHelp          -> Shows the lines of text above')
        ans += str('\nPrices        -> Only available through the Shop menu. '
                   'shows prices for water, food and space')
        ans += str('\nRename        -> Renames your restaurant to a new'
                   ' name\n')
        ans += 'ED            -> Error Documentation. Tells you how to'\
               ' fix a bug or problem\n'

        return ans

    def about(self):
        """ Tells the info of the program """
        ans = ''
        ans += str(f'\n{VERSION}')
        ans += str(f'\nReleased on {VERSION_DATE}')
        ans += str('\nCopyright © Alvin Ran. All rights reserved\n')
        ans += str('\nMade by Alvin\n')
        ans += str('\nContributors:')
        ans += str('\nJun\nZhiping\n')
        return ans
