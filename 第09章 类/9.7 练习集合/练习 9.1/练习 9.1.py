class Restaurant:

	def __init__(self, restaurant_name, cuisine_name):
		self.restaurant_name = restaurant_name
		self.cuisine_name = cuisine_name

	def describe_restaurant(self):
		print(f"The name of this restaurant is {self.restaurant_name}.")
		print(f"The cuisine type of this restaurant is {self.cuisine_name}.")

	def open_restaurant(self):
		print("The restaurant is open.")

new_restaurant = Restaurant("Lu flavour", 'Lu')

# 分别打印其两个属性。
print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_name)

# 调用类方法。
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()