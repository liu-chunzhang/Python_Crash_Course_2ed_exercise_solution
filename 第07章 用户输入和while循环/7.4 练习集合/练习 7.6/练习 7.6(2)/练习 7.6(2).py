# 练习 7.6的第二种思路：使用变量active来控制循环结束的时机。
active = True
while active :
	topping = input("You can add a kind of pizzatoppings, if not, please input 'quit': ")
	if topping == 'quit':
		active = False
	else :
		print(f"We will add {topping}.")