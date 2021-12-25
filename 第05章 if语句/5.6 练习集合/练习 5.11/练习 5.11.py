numbers = list(range(1,10))

# 5.11(2)的要求和5.11(3)的要求放在一起处理。
for num in numbers:
	if num == 1 :
		print("1st")
	elif num == 2 :
		print("2nd")
	elif num == 3 :
		print("3rd")
	else :
		print(f"{num}th")