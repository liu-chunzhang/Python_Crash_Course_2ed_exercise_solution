user_names = ['admin', 'Amy', 'Bob', 'David', 'Jack', 'Tom']

if user_names :
	for user_name in user_names:
		if user_name == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {user_name}, thank you for logging in again.")
else :
	print("We need to find some users!")

user_names = []
if not user_names :
	print("We need to find some users!")