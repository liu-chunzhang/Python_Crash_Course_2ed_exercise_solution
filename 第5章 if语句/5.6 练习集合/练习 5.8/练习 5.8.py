user_names = ['admin', 'Amy', 'Bob', 'David', 'Jack', 'Tom']

for user_name in user_names:
	if user_name == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {user_name}, thank you for logging in again.")