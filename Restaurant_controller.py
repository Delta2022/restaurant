""" Contains the class for controller """
ANS_OVERRIDE = ''
try:
    from Restaurant_model import Model
except ModuleNotFoundError:
    ANS_OVERRIDE = ('\nPlease put Restaurant_Model.py and'
                    ' Restaurant_Controller.py together in the same folder\n')


class Controller:
    """ The Controller class of the Restaurant """
    def __init__(self, name=""):
        """ init of controller class """
        if not ANS_OVERRIDE:
            self.aiyo = Model(name)
            self.ans = ''
            self.ans2 = ''
            self.ans3 = ''
            self.ans1 = ''
            self.thing = ''
            self.save_successful = ''

    def request(self, string):
        """ Takes in a request from restaurant_view.py and sends it to \
        restaurant_model.py """
        if not ANS_OVERRIDE:
            str.lower(string)
            if string == 'open':
                ans = self.aiyo.r_open()
                self.ans2 = ans

            elif string == 'save':
                self.save_successful = self.aiyo.r_save()
                self.ans2 = self.save_successful

            elif string == 'info':
                ans = self.aiyo.r_describe
                self.ans2 = ans

            elif string == 'shop':
                prompt1 = self.aiyo.r_buy('prices') + '\nWhat do you want to'\
                    ' buy?  '
                string2 = input(prompt1)
                string2 = str.lower(string2)

                if string2 == 'food':
                    self.ans2 = self.aiyo.r_buy('food')
                elif string2 == 'water':
                    self.ans2 = self.aiyo.r_buy('water')
                elif string2 == 'space':
                    self.ans2 = self.aiyo.r_buy('limit')
                elif string2 in ('prices', 'price'):
                    self.ans2 = self.aiyo.r_buy('prices')
                else:
                    self.ans2 = 'What?'

            elif string == 'rename':
                string2 = input('Enter the new name:  ')
                self.ans1 = self.aiyo.rename(string2)
                self.ans2 = self.ans1

            elif string in ('help', 'h'):
                self.ans1 = self.aiyo.help()
                self.ans2 = self.ans1
            elif string == 'about':
                self.ans2 = self.aiyo.about()
            elif string == 'ed':
                string3 = '1. Unsuccessful Saves\n2. Unsuccessful Resets\n\n' \
                    'Enter a number that\'s '\
                    'in front of what you want:  '
                string2 = input(string3)
                string2 = str.lower(string2)
                if string2 == '1':
                    self.ans2 = self.aiyo.ed('#1')
                elif string2 == '2':
                    self.ans2 = self.aiyo.ed('#2')
                else:
                    self.ans2 = 'What?'

            else:
                self.ans2 = 'What?'

            if ANS_OVERRIDE:
                self.ans2 = ANS_OVERRIDE
            self.ans3 = self.ans2
        else:
            self.ans3 = ANS_OVERRIDE
        return self.ans3
