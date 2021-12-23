class Restaurant:

	def __init__(self, restaurant_name , cuisine_name):
		self.restaurant_name = restaurant_name
		self.cuisine_name = cuisine_name
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The name of this restaurant is {self.restaurant_name}.")
		print(f"The cuisine type of this restaurant is {self.cuisine_name}.")

	def open_restaurant(self):
		print("The restaurant is open.")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, increment_number_served):
		self.number_served += increment_number_served


class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, *flavors):
		# 初始化父类的属性。
		super().__init__(restaurant_name, 'ice cream')
		# 初始化IceCreamStand类的特有属性。
		self.flavors = flavors

	def flavors_print(self):
		message = "The ice cream shop has "
		for flavor in self.flavors :
			if flavor != self.flavors[-1]:
				message += f"{flavor} ice cream, "
			else :
				message += f"{flavor} ice cream."
		print(message)

ice_cream_shop = IceCreamStand("Mixuebingcheng", 'creamy', 'chocolate', 'matcha')
ice_cream_shop.flavors_print()