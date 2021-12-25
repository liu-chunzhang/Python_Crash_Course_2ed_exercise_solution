# 练习 7.6的第一种思路：在while循环中使用条件测试来结束循环。
topping = input("You can add a kind of pizzatoppings, if not, please input 'quit': ")
while topping != 'quit' :
	print(f"We will add {topping}.")
	topping = input("You can add a kind of pizzatoppings, if not, please input 'quit': ")