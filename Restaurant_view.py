# Version Info in Restaurant_model.py
# TODO: Check Restaurant for bugs and/or errors
""" Contains the view part of MVC """
from json import load, dump, decoder
from time import sleep
from datetime import date
from os import path

JSON_FILE = path.abspath(__file__)
JSON_FILE = JSON_FILE.replace('Restaurant_view.py', '.Restaurant.json')
MNFE1 = ''
DATE = date.today().day
JSON_DICT = {
                    "name": "",
                    "quality": 1,
                    "age": {"year": 2008, "month": 2, "day": 27, "dow":
                            date.today().weekday()},
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

try:
    from Restaurant_controller import Controller
except ModuleNotFoundError:
    print('\nPlease put Restaurant_controller.py and Restaurant_view.py'
          ' together in the same folder\n')
    MNFE1 = 'True'

try:
    with open(JSON_FILE) as f1:  # Loads the .Restaurant.json code
        content = load(f1)
except (decoder.JSONDecodeError, FileNotFoundError):  # If there is no
    # code, it puts in the code
    with open(JSON_FILE, 'w') as f1:
        dump(JSON_DICT, f1)
    with open(JSON_FILE) as f1:
        content = load(f1)

if MNFE1 == '':  # if .Restaurant.json doesn't exist, it tells the user.
    if content['name'] == '':

        name = input('Welcome! Please enter your restaurant\'s name:  ')
        print('\nType \'help\' to show all commands and a brief description'
        ' of each command.')

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
            sleep(4)
            print(ans[1])
        elif REQUEST == 'reset':
            STRING1 = input('Are you sure?  ')
            STRING1 = str.lower(STRING1)
            if MNFE1 == '':
                with open(JSON_FILE, 'w') as temp_file:
                    dump(JSON_DICT, temp_file)
                print('\nReset successful\n')
                break
            else:
                print('\nReset unsuccessful (ED #2)\n')

        else:
            ans = controller.request(REQUEST)
            print(ans)

print('The End\n')
