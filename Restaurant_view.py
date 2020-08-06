""" Contains the view part of MVC """
import json
import time

MNFE1 = ''
try:
    from restaurant_controller import Controller
except ModuleNotFoundError:
    print('\nPlease put Restaurant_controller.py and Restaurant_view.py'
          ' together in the same folder\n')
    MNFE1 = 'True'

try:
    with open('/Users/alvinran/Restaurant/Restaurant.json') as f1:
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
        "a_25_space": "False"
        }


if not MNFE1:
    if content['name'] == '':

        name = input('Welcome! Please enter your restaurant\'s name:  ')

    else:
        name = content['name']
        print(f'\nWelcome back to your restaurant: {name}')

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
        else:
            ans = controller.request(REQUEST)
            print(ans)

print('The End\n')
