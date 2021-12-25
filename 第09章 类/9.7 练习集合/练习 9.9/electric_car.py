class Car:
	""" 一次模拟汽车的简单尝试。 """

	def __init__(self, make, model, year):
		""" 初始化描述汽车的属性。 """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		""" 返回整洁的描述性信息。 """
		longname = f"{self.year} {self.make} {self.model}"
		return longname.title()

	def read_odometer(self):
		""" 打印一条能指出汽车里程的消息。 """
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""
		将里程表读数设置为指定的值。
		禁止将里程表读书往回调。
		"""

		if mileage >= self.odometer_reading:
			""" 将里程表读数设置为指定的值。 """
			self.odometer_reading = mileage
		else :
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""
		将里程表读数增加指定的正值。
		禁止将里程表读书往回调。
		"""

		if miles < 0 :
			print("You can't roll back an odometer!")
		else:
			""" 将里程表增加指定的量。 """
			self.odometer_reading += miles


class Battery:
	""" 一次模拟电动汽车电瓶的简单尝试。 """

	def __init__(self, battery_size = 75):
		""" 初始化电瓶的属性。 """
		self.battery_size = battery_size

	def describe_battery(self):
		""" 打印一条描述电瓶容量的消息。 """
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		""" 打印一条消息，指出电瓶的续航里程。 """
		if self.battery_size == 75 :
			range = 260
		elif self.battery_size == 100 :
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		if self.battery_size != 100 :
			self.battery_size = 100


class ElectricCar(Car):
	""" 电动汽车的独特之处。 """

	def __init__(self, make, model, year):
		""" 
		初始化父类的属性。
		再初始化电动汽车特有的属性。
		"""
		super().__init__(make, model, year)
		self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()