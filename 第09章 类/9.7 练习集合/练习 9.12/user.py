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