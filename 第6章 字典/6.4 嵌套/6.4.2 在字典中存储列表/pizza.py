# 存储所点批萨的信息。
pizza = {
	'crust': 'thick',
	'toppings':['mushrooms', 'extra cheese']
	}

# 概述所点的批萨。
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)