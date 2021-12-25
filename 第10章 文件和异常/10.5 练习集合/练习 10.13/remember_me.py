# 本题基本重构了原有架构，因此连函数名都改了。
import json

def get_stored_username():

	usernames = 'user_name.json'
	try :
		with open(usernames) as f:
			names = json.load(f)
	except FileNotFoundError:
		create_names(usernames)
	else :
		add_names(usernames,names)

def create_names(filename):
	name = input("Please input your name. ")
	with open(filename, 'w') as fn:
		names = [name]
		json.dump(names,fn)
		print(f"We'll store your name.")

def add_names(filename,names):
	name = input("Please input your name. ")
	if name in names :
		print(f"Welcome back, {name}!")
	else :
		names.append(name)
		with open(filename, 'w') as fn:
			json.dump(names,fn)
		print(f"We will store your name, {name}.")

def greet_user():
	get_stored_username()

greet_user()