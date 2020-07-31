from Restaurant_model import Model

class Controller:
	def __init__(self,name=""):
		self.aiyo = Model(name)

	def request(self,string):
		str.lower(string)
		if string == 'open':
			ans = self.aiyo.r_open()
			return ans
		
		elif string == 'save':
			self.aiyo.r_save()
			return '\nProgress Saved\n'
		
		elif string == 'info':
			ans = self.aiyo.r_describe()
			return ans

		elif string == 'shop':
			string2 = input('What do you want to buy?  ')
			string2 = str.lower(string2)

			if string2 == 'food':
				self.aiyo.r_buy('food')
			elif string2 == 'water':
				self.aiyo.r_buy('water')
			elif string2 == 'space':
				self.aiyo.r_buy('limit')
			elif string2 == 'prices' or string2 == 'price':
				self.aiyo.r_buy('prices')
			else:
				return 'What?'

		elif string == 'rename':
			string2 = input(f'Enter the new name:  ')
			a = self.aiyo.rename(string2)
			return a

		elif string == 'help' or string == 'h':
			a = self.aiyo.help()
			return a
		
		else:
			return 'What?'