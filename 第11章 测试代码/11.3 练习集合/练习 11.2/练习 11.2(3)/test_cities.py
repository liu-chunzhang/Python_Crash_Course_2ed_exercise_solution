# 练习11.2(3)的要求：修改函数city_in_country加入可选形参population，并修改测试。
import unittest
from city_functions import city_in_country

class CityTestCase(unittest.TestCase):
	""" 测试city_function.py。 """

	def test_city_country(self):
		""" 测试能否正确处理像Santiago, Chile的实例吗？ """
		city_and_country = city_in_country('Santiago', 'Chile')
		self.assertEqual(city_and_country, 'Santiago, Chile')

	def test_city_country_population(self):
		""" 测试能否正确处理像Santiago, Chile population=5000000的实例吗？ """
		city_and_country = city_in_country('Santiago', 'Chile', '5000000')
		self.assertEqual(city_and_country, 'Santiago, Chile - Population 5000000')

if __name__ == "__main__" :
	unittest.main()