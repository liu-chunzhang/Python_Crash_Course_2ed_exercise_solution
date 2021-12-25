from user import User

class Privileges:

	# Privileges类的初始化函数。
	def __init__(self, *privilege):
		self.privileges = privilege

	# 方法show_privileges的定义。
	def show_privileges(self):
		message = "The privileges of admin "
		if len(self.privileges) == 0 :
			message += "don't exist."
		elif len(self.privileges) == 1 :
			message += "is: "
		else :
			message += "are: "
		print(message)

		for privilege in self.privileges:
			print(f"- {privilege}")


class Admin(User):

	def __init__(self, last_name, first_name, age, education_background):
		super().__init__(last_name, first_name, age, education_background)
		self.privileges = Privileges('can add post', 'can delete post', 'can ban user')

	def show_privileges(self) :
		self.privileges.show_privileges()