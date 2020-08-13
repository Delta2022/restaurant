""" Contains the class for the Model """
import random
from json import load, dump
from datetime import date

VERSION = 'Version 1.2.9 pre-3 unstable'
VERSION_DATE = 'August 8 2020'
DATE = date.today().day
class Model:
    """ The Model class of the Restaurant """
    def __init__(self, name=""):
        """ JSON reading and all var defined here """
        self.json_file = '/home/pi/restaurant/Restaurant.json'
        try:
            with open(self.json_file) as temp_file:
                self.file = load(temp_file)
                self.save = True
        except FileNotFoundError:
            self.save = False
            self.file = {
                "name": "",
                "quality": 1,
                "age": 0,
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
                "limit": 10,
                "p_limit": 75,
                "a_25_space": "False",
                "date": DATE + 1
                }
        self.name = name
        self.quality = self.file['quality']
        self.age = self.file['age']
        self.totalcustomers = self.file['totalcustomers']
        self.money = float(self.file['money'])
        self.add3 = 0
        self.food = self.file['food']
        self.water = self.file['water']
        self.p_water = self.file['p_water']
        self.p_food = self.file['p_food']
        self.e_water = float(self.file['e_water'])
        self.e_food = float(self.file['e_food'])
        self.expences = float(self.e_water + self.e_food)
        self.a_100_totalcustomers = self.file['a_100_totalcustomers']
        self.a_100_totalmoney = self.file['a_100_totalmoney']
        self.a_20_totalmoney = self.file['a_20_totalmoney']
        self.a_25_space = self.file['a_25_space']
        self.limit = self.file['limit']
        self.p_limit = float(self.file['p_limit'])
        self.saved = 0
        self.gst = 0
        self.add1 = 0
        self.add2 = 0
        self.add3 = 0
        if self.file['date'] == DATE:
            self.money += 50

    def r_open(self):
        """ Opens the Restaurant """
        ans = ''
        ans1 = ''
        list1 = []
        ans1 += str(f'\n\n{self.name} is open!')
        ans1 += str('\n(you can only open once per day)\n')
        ans1 += str('\n\n...\n')
        self.add1 = random.randrange(0, 2*self.food + 12)
        if self.add1 > self.limit:

            if self.add1 - self.limit == 1:
                ans += str('\nYou have not enough space! 1 person is in queue')
            else:
                ans += str(f'\nYou have not enough space!'
                           f' {self.add1 - self.limit} people are in queue')
            if self.food - 6 < self.add1 - self.limit:
                if self.food - 1 != self.add1 - self.limit - 1:
                    self.saved = random.randrange(self.food - 1, self.add1 -
                                                  self.limit-1, 1)
                else:
                    self.saved = 0
            else:
                self.saved = random.randrange(self.add1 - self.limit - 5,
                                              self.add1 - self.limit-1, 1)
            if self.saved > 0:
                if self.saved == 1:
                    ans += str('\n1 person waited but'
                               f' {self.add1 - self.limit - self.saved} people'
                               ' left\n')
                else:
                    ans += str(f'\n{self.saved} people waited but '
                               f'{self.add1 - self.limit - self.saved} left\n')
            else:
                ans += str('\nEverybody left\n')
            self.add1 = self.limit + self.saved
        self.totalcustomers += self.add1
        self.age += 1
        ans += str(f'\n{self.add1} people entered {self.name} today!')
        if self.a_100_totalcustomers == "False" and self.totalcustomers >= 100:
            ans += str('\n\nYou have unlocked an achievement: '
                       '\'Popular Restaurant\' '
                       '( Have 100 customers total visit your restaurant )\n')
            self.a_100_totalcustomers = "True"
        for i in range(self.add1):
            self.add2 = float(random.randrange(1, 2*self.water + 5))
            self.add3 = float(self.add3)
            self.gst = self.add2 * 0.05
            self.add2 = round(1.05*self.add2, 2)
            self.add3 += self.add2
            self.money += self.add2
        ans += str(f'\n\nYou earned ${"%.2f"%self.add3} + GST for a total of'
                   f' ${"%.2f"%self.money}\n')
        self.add3 = 0

        ans += str(f'\nYou need ${"%.2f"%self.expences} to pay for your '
                   'expences\n')
        self.money -= self.expences
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
        self.add1 = 0
        ans += str(f'\n{self.name} is closed\n')

        list1 = [ans1, ans]

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
                    "limit": self.limit,
                    "p_limit": self.p_limit,
                    "a_25_space": str(self.a_25_space),
                    "date": DATE + 1
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
                    self.expences = float(self.e_water + self.e_food)
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
                    self.expences = float(self.e_water + self.e_food)
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
        ans += str(f'\nYour Restaurant {self.name}\'s infomation:\n')

        if self.age == 1:
            ans += str(f'\nAge                      =  {self.age} day')
        else:
            ans += str(f'\nAge                      =  {self.age} days')
        ans += str(f'\nDaily Expences           =  ${"%.2f"%self.expences}')
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
        ans += str('\nInfo          -> Gives infomation about your '
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
        ans += 'ED            -> Error Documentaion. Tells you how to'\
            ' fix a bug or problem'
        return ans

    def about(self):
        """ Tells the info of the program """
        ans = ''
        ans += str(f'\n{VERSION}')
        ans += str(f'\nReleased on {DATE}')
        ans += str('\nCopyright © Alvin Ran. All rights reserved\n')
        ans += str('\nMade by Alvin Ran')
        ans += str('\nContributors:')
        ans += str('\nJun Ran\nZhiping Lou\n')
        return ans

    def ed(self, item):
        """ Error Documents """

        ans = ''
        if item == '#1':
            ans = '\nSave Error:\n\nRestaurant has a single-slot save' \
                ' system, The system uses a json file to store all the' \
                ' info it needs to run the next time you want to play'  \
                '.\n\nTo fix the \'Unsuccessful Save\'' \
                ' error, you need to make a file ending with \'.json\'.\n' \
                ' After making the file, you need to find the directory' \
                ' for the file you just made (if you don\'t know how to,' \
                ' search it up) and paste it into the json_file variables' \
                ' at the start of Restaurant_model.py and' \
                ' Restaurant_view.py.\nAfter doing that, paste \n\n{ '\
                '"name": "", '\
                '"quality": 1, '\
                '"age": 0, '\
                '"totalcustomers": 0, '\
                '"money": 50, '\
                '"food": 1, '\
                '"water": 1, '\
                '"p_food": 100, '\
                '"p_water": 75, '\
                '"e_water": 2, '\
                '"e_food": 2, '\
                '"a_100_totalcustomers": "False",'\
                '"a_100_totalmoney": "False",'\
                '"a_20_totalmoney": "False",'\
                '"limit": 10,'\
                '"p_limit": 75,'\
                '"a_25_space": "False",'\
                '"date": (Put the day of the month here)' \
                '}\n\ninto the file.\n\nCreated by: Alvin Ran\nReleased ' \
                'on Friday August 7 2020\n'
        elif item == '#2':
            ans = '\nReset Error\n\nIf Resets fail, that\'s because the'\
            ' program doesn\'t save when you exit. To fix it, go to #1 on ED'\
            '\n\nCreated by: Alvin Ran\nReleased on Saturday August 8 2020\n'
        else:
            ans += 'What?'
        return ans
