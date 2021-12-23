# 5.10(1)的要求：创建一个至少包含5个用户名的列表，并将其命名为current_users 
current_users = ['Amy', 'Bob', 'David', 'Jack', 'List']

# 5.10(2)的要求：再创建一个至少包含5个用户名的列表，并将其命名new_users，并确保其中有一两个用户名也包含在列表current_users中 
new_users = ['Bob', 'Thomas', 'Stein', 'LIST', 'Eric']

# 5.10(3)的要求：对于其中的每个用户名，都检查它是否已被使用。如果是，就打印一条信息，指出需要输入别的用户名；否则，打印一条信息，指出这个用户名未被使用。
# 5.10(4)的要求：确保比较时不区分大小写。
current_users2 = [ current_user.lower() for current_user in current_users ]

for new_user in new_users:
	if new_user.lower() in current_users2:
		print(f"Sorry, username '{new_user}' is used, and you should find another username.")
	else:
		print(f"Conguratulation, username '{new_user}' is unused.")