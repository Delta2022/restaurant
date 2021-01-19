# Version Info in Restaurant_model.py
""" Contains the view part of MVC """
from json import load, dump, decoder
from time import sleep
from datetime import date
from os import path
import PySimpleGUI as sg

# PySimpleGUI Variables
layout = [
    [sg.Text('no output',size=(50,None), key='text')],
    [sg.Input(key='input')],
    [sg.Button('Read', key='read')]
]
window = sg.Window('Restaurant', layout, finalize=True)

# Normal files
JSON_FILE = path.abspath(__file__)
JSON_FILE = JSON_FILE.replace('_gui.py', '.json')
JSON_FILE = JSON_FILE.replace('_view', '')
JSON_FILE = JSON_FILE.replace('R', '.R')
MNFE1 = ''
REQUEST = ''
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
    window['text'].update('\nPlease put Restaurant_controller.py and Restaurant_view.py'
          ' together in the same folder\n')
    sleep(5)
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

if MNFE1 == '':  # if .Restaurant.json doesn't exist, it does stuff
    if content['name'] == '':
        window['text'].update('Please enter name below:')
        event, values = window.read()
        REQUEST = values['input']


        name = REQUEST
        print(name) # debugging
        print(REQUEST) # debugging
        # TODO: Make the website be able to save-ish
        ans = ('\nType \'help\' to show all commands and a brief description.'
              ' If you encounter a problem, type \'ed\' for solutions\n\n')

    else:
        # Unsure if works, try after fixed saving
        name = content['name']
        ans = (f'\nWelcome back to your restaurant: {name}\n\n')
        if content['date'] == DATE and content["streak"] > 1:
            ans += (f'\nCongratulations for playing {content["streak"]} days'
                  ' in a'
                  f' row! For that I\'ll give you {content["streak"] * 10}'
                  f' dollars!\n\n')

    controller = Controller(name)
    ans += controller.request('info')
    window['text'].update(ans)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            ans = controller.request('save')
            print('saved') # debugging
            break
        if ans == '\nPlease put Restaurant_Model.py and' \
                  ' Restaurant_Controller.py together in the same folder\n':
            break
        if event == 'read':
            REQUEST = values['input']
            print(REQUEST)  # Remove this later, it's for debugging purposes
            window['text'].update(REQUEST)
            # TODO: Fix shop command
        REQUEST = str.lower(REQUEST)

        if REQUEST == 'exit':
            # window['text'].update('The end')
            ans = controller.request('save')
            window['text'].update(ans)
            break

        if REQUEST == 'open':
            ans = controller.request('open')
            window['text'].update(ans[0])
            sleep(4)
            window['text'].update(ans[1])
        # TODO: Fix reset
        elif REQUEST == 'reset':
            window['text'].update('Are you sure?')
            event, values = window.read()
            STRING1 = values['input']

            STRING1 = str.lower(STRING1)
            if STRING1 in ('yes', 'y'):
                if MNFE1 == '':
                    with open(JSON_FILE, 'w') as temp_file:
                        dump(JSON_DICT, temp_file)
                    window['text'].update('\nReset successful\n')
                    break
            window['text'].update('\nReset unsuccessful \n')

        else:
            ans = controller.request(REQUEST)
            window['text'].update(ans)

window.close()
