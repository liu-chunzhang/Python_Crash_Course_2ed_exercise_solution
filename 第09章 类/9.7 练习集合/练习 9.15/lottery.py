from random import choice

contents = ('a', 'b', 'c', 'd', 'e', '1', '2', 
		'3', '4', '5', '6', '7', '8', '9', '0'
		  )

my_ticket = ['6174']
countnum = 0

while True:
	message = ""
	for i in range(4):
		message += choice(contents)
	countnum += 1
	if message in my_ticket:
		break

print(f"You need {countnum} times to hit the jackpot!")