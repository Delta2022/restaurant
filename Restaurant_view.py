# Version Info in Restaurant_model.py

""" Contains the view part of MVC """
import json
import time
from datetime import date

JSON_FILE = '/Users/alvinran/Restaurant/Restaurant.json'
MNFE1 = ''
DATE = date.today().day
try:
    from Restaurant_controller import Controller
except ModuleNotFoundError:
    print('\nPlease put Restaurant_controller.py and Restaurant_view.py'
          ' together in the same folder\n')
    MNFE1 = 'True'

try:
    with open(JSON_FILE) as f1:
        content = json.load(f1)
except FileNotFoundError:
    content = {
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
        "time": date.today().day + 1
        }

if MNFE1 == '':
    if content['name'] == '':

        name = input('Welcome! Please enter your restaurant\'s name:  ')
        print('\nType \'help\' to show all commands and a brief description'
              ' If you encounter a problem, type \'ed\' for solutions')

    else:
        name = content['name']
        print(f'\nWelcome back to your restaurant: {name}')
        if content['date'] == DATE:
            print('Contradulations! For playing for at least 2 days in a '
                'row! For that I\'ll give you 50 dollars!')

    controller = Controller(name)
    ans = controller.request('info')
    print(ans)

    while True:
        if ans == '\nPlease put Restaurant_Model.py and' \
        ' Restaurant_Controller.py together in the same folder\n':
            break

        REQUEST = input('What do you want to do?  ')
        REQUEST = str.lower(REQUEST)

        if REQUEST == 'exit':
            ans = controller.request('save')
            print(ans)
            break

        if REQUEST == 'open':
            ans = controller.request(REQUEST)
            print(ans[0])
            time.sleep(4)
            print(ans[1])
        elif REQUEST == 'reset':
            STRING1 = input('Are you sure?  ')
            STRING1 = str.lower(STRING1)
            if MNFE1 == '':
                with open(JSON_FILE, 'w') as temp_file:
                    json.dump({
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
                        "a_25_space": "False"
                        }, temp_file)
                print('\nReset successful\n')
                break
            else:
                print('\nReset unsuccessful (ED #2)\n')


        else:
            ans = controller.request(REQUEST)
            print(ans)

print('The End\n')
