# 练习 7.6的第三种思路：使用break语句在用户输入'quit'时退出循环。此处直接拷贝的练习 7.4，因为本来就是用while循环写的。
while True :
	topping = input("You can add a kind of pizzatoppings, if not, please input 'quit': ")
	if topping == 'quit':
		break
	else :
		print(f"We will add {topping}.")