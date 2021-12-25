age = int(input(f"Please input your age, then the ticket price will be given according to your input age. "))

if age < 0 :
	print("The age you input is not valid!")
elif age < 3 :
	print("Your are free.")
elif age < 13 :
	print("Your ticket price is $10.")
else :
	print("Your ticket price is $15.")