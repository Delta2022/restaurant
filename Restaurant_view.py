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
except json.decoder.JSONDecodeError:
    with open(JSON_FILE, 'w') as f1:
        json.dump({
                    "name": "",
                    "quality": 1,
                    "age": {"year": 2008, "month": 2, "day": 27},
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
                    "date": DATE + 1,
                    "streak": 0
                    }, f1)
    with open(JSON_FILE) as f1:
        content = json.load(f1)
except FileNotFoundError:
    content = {
        "name": "",
        "quality": 1,
        "age": {"year": date.today().year, "month": date.today().month,
                "day": date.today().day},
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
        "time": date.today().day + 1,
        "streak": 0
        }

if MNFE1 == '':
    if content['name'] == '':

        name = input('Welcome! Please enter your restaurant\'s name:  ')
        print('\nType \'help\' to show all commands and a brief description'
              ' If you encounter a problem, type \'ed\' for solutions')
        age = {date.today().year, date.today().month, date.today().day}

    else:
        name = content['name']
        print(f'\nWelcome back to your restaurant: {name}')
        if content['date'] == DATE and content["streak"] > 1:
            print(f'Congratulations for playing {content["streak"]} days'
                  ' in a'
                  f' row! For that I\'ll give you {content["streak"] * 10}'
                  f' dollars!')

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
                        "age": {"year": 2008, "month": 2, "day": 27},
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
                        "date": DATE + 1,
                        "streak": 0
                        }, temp_file)
                print('\nReset successful\n')
                break
            else:
                print('\nReset unsuccessful (ED #2)\n')

        else:
            ans = controller.request(REQUEST)
            print(ans)

print('The End\n')
