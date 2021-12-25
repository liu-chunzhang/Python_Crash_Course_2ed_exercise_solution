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

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()