from Restaurant_controller import Controller
import json
import time

with open('/Users/alvinran/Restaurant/Restaurant.json') as f1:
	content = json.load(f1)

if content['name'] == '':

	name = input('Welcome! Please enter your restaurant\'s name:  ')

else:
	name = content['name']
	print(f'\nWelcome back to your restaurant: {name}')

controller = Controller(name)
ans = controller.request('info')
print(ans)

while True:
	request = input('What do you want to do?  ')
	request = str.lower(request)

	if request == 'exit':
		ans = controller.request('save')
		print(ans)
		break
	
	if request == 'open':
		ans = controller.request(request)
		print(ans[0])
		time.sleep(4)
		print(ans[1])
	else:
		ans = controller.request(request)
		print(ans)

print('The End\n')