filename = 'guest.txt'

with open(filename,'a') as fn :
	message = input("Hello, newbie. Please enter your name for record. ")
	fn.write(f"{message}\n")