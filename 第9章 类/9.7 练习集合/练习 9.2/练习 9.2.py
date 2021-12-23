class Restaurant:

	def __init__(self, restaurant_name, cuisine_name):
		self.restaurant_name = restaurant_name
		self.cuisine_name = cuisine_name

	def describe_restaurant(self):
		print(f"The name of this restaurant is {self.restaurant_name}.")
		print(f"The cuisine type of this restaurant is {self.cuisine_name}.")

	def open_restaurant(self):
		print("The restaurant is open.")

new_restaurant1 = Restaurant("Lu flavour", 'Lu')
new_restaurant2 = Restaurant("Xiang flavour", 'Xiang')
new_restaurant3 = Restaurant("Chuan flavour", 'Chun')

new_restaurant1.describe_restaurant()
print()
new_restaurant2.describe_restaurant()
print()
new_restaurant3.describe_restaurant()