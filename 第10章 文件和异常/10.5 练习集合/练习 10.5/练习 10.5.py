filename = 'reasons.txt'

while True:
	with open(filename,'a') as fn :
		message = input("Why do you like programming? ")
		fn.write(f"{message.title()}\n")
	flag = input("Thanks, and other reasons?(yes/no) ")
	if flag == 'no':
		break