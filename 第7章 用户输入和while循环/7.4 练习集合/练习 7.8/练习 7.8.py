sandwich_orders = ['egg sandwich', 'pastrami sandwich', 'bacon sandwich', 'pastrami sandwich', 'pastrami sandwich', 'beef sandwich', 'tuna sandwich']
finished_sandwiches = []

while sandwich_orders:
	sandwich_name = sandwich_orders.pop(0)
	print(f"I made your {sandwich_name}.")
	finished_sandwiches.append(sandwich_name)

print("I have made all kinds of sandwiches.")
for sandwich_name in finished_sandwiches :
	print(sandwich_name)