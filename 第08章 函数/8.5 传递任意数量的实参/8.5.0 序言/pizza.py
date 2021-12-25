def make_pizza(*toppings):
	""" 概述要制作的批萨。 """
	print("\nMaking a pizza with the fowwowing toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')