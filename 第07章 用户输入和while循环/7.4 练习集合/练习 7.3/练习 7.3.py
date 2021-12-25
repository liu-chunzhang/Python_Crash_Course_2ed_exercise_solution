inputnumber = input("Please input an integer number: ")

if int(inputnumber) % 10 == 0 :
	message = f"The number {inputnumber} is a multiple of 10."
else :
	message = f"The number {inputnumber} is not a multiple of 10."
	
print(message)