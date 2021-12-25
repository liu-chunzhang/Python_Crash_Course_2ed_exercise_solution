# 为了复用代码，特别定义了一个函数用于打印含批萨的列表
def pizzaprint(list):
	for item in list:
		print(item)

my_pizzas = ['bacon pizza', 'shrimp pizza', 'cheese pizza', 'durian pizza' ]
friend_pizzas = my_pizzas[:]

# 4.11(1)的要求：在原来的批萨列表中再添加一种批萨。
my_pizzas.append("fruit pizza")

# 4.11(2)的要求：在列表friend_pizzas中添加另一种批萨。
friend_pizzas.append("beef pizza")

# 4.11(3)的要求：核实有两个不同的列表。
print("My favorite foods are:")
pizzaprint(my_pizzas)

print("\nMy friend's favorite foos are:")
pizzaprint(friend_pizzas)