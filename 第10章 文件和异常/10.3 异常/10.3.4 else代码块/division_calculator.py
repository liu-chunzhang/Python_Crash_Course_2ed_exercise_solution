print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q' :
		break
	second_number = input("Second number: ")
	if second_number == 'q' :
		break
	try :
		answer = int(first_number) / int(second_number)
		# answer = float(first_number) / float(second_number) 	 这里感觉换成float(first_number)/float(second_number)更合适
	except ZeroDivisionError :
		print("You can't divide by 0!")
	else :
		print(answer)