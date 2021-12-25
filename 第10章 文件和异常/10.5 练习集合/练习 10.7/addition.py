print("The programming is to supply the addition of two numbers.")
while True:
	try :
		num1 = float(input("Please input the first number: "))
		num2 = float(input("Please input the second number: "))
	except ValueError :
		print("At least one of what you input is not a number!")
	else :
		result = num1 + num2
		print(f"The result of the addition of {num1} and {num2} is {result}.")
	flag = input("If you want to continue?(yes/no) ")
	if flag == 'no':
		break