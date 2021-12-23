from random import choice

contents = ('a', 'b', 'c', 'd', 'e', '1', '2', 
		'3', '4', '5', '6', '7', '8', '9', '0'
		  )

message = ""
for i in range(4):
	message += choice(contents)

print(f"If you get {message}, you hit the jackpot!")