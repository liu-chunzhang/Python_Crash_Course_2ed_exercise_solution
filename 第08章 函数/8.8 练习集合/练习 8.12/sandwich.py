def sandwich_toppings(*toppings):
	message = "The sandwich toppings "
	if len(toppings) == 0:
		message += "doesn't exist."
	elif len(toppings) == 1:
		message += 'is:'
	else :
		message += 'are:'
	print(message)

	for topping in toppings:
		print(f"- {topping}")

sandwich_toppings('bacon', 'beef', 'tomato')
sandwich_toppings('green peppers', 'mushroom', 'potato')
sandwich_toppings('extra cheese')
sandwich_toppings()