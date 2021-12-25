import json

try:
	filename = 'favorite_numbers.json'
	with open(filename) as fn :
		numbers = json.load(fn)
except FileNotFoundError:
	pass
else :
	for number in numbers:
		print(number)