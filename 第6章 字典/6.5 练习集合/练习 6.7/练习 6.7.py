man = { 
	'first_name': 'List',
	'last_name': "David", 
	"age": 38, 
	'city': "New York"
	}

man2 = { 
	'first':'albert',
	'last':'einstein',
	'age': 67,
	'location':'princeton'
	}

man3 = {
	'first':'marie', 
	'last': 'curie', 
	'age': 25,
	'location': 'paris'
	}

people = [man, man2, man3]

for man in people :
	for name, term in man.items():
		print(f"{name}: {term}.")
	print()