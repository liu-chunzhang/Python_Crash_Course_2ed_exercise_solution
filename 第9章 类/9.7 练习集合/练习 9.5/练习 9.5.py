class User:

	def __init__(self, last_name, first_name, age, education_background):
		self.last_name = last_name
		self.first_name = first_name
		self.age = age
		self.education_background = education_background
		self.login_attempts = 0

	def describe_user(self):
		print(f"The name of user is {self.first_name} {self.last_name}.")
		print(f"User's age is {self.age}.")
		print(f"User's education background is {self.education_background}.")

	def greet_user(self):
		print(f"Hello, {self.first_name} {self.last_name}.")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

Amy_David = User('Amy', 'David', 18, 'bachelor')
Bob_Macmillin = User('Bob', 'Macmillin', 23, 'master')

Amy_David.greet_user()
Bob_Macmillin.describe_user()

# 令Amy调用increment_login_attempts共4次，并打印其login_attempts属性。
for i in range(1, 5):
	Amy_David.increment_login_attempts()
print(Amy_David.login_attempts)

# 令Amy调用reset_login_attempts，清零其login_attempts属性。
Amy_David.reset_login_attempts()
print(Amy_David.login_attempts)