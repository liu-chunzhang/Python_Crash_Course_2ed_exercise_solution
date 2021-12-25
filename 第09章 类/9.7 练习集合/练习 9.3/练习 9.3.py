class User:

	def __init__(self, last_name, first_name, age, education_background):
		self.last_name = last_name
		self.first_name = first_name
		self.age = age
		self.education_background = education_background

	def describe_user(self):
		print(f"The name of user is {self.first_name} {self.last_name}.")
		print(f"User's age is {self.age}.")
		print(f"User's education background is {self.education_background}.")

	def greet_user(self):
		print(f"Hello, {self.first_name} {self.last_name}.")

# 创建User类的实例
Amy_David = User('Amy', 'David', 18, 'bachelor')
Bob_Macmillin = User('Bob', 'Macmillin', 23, 'master')

# 调用User类的方法
Amy_David.greet_user()
Bob_Macmillin.describe_user()