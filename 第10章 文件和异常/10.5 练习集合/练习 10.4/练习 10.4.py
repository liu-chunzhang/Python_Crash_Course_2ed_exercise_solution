filename = 'guest.txt'

while True:
	with open(filename,'a') as fn :
		message = input("Hello, newbie. Please enter your name for record. ")
		print(f"Hello, {message.title()}!")
		fn.write(f"{message.title()}\n")