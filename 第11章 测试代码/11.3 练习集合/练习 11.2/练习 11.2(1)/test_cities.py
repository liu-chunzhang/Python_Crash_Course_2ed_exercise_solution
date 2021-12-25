# 练习11.2(1)的要求：只修改函数city_in_country加入必不可少的形参population，但不修改测试。
import unittest
from city_functions import city_in_country

class CityTestCase(unittest.TestCase):
	""" 测试city_function.py。 """

	def test_city_country(self):
		""" 测试能否正确处理像Santiago, Chile的实例吗？ """
		city_and_country = city_in_country('Santiago', 'Chile')
		self.assertEqual(city_and_country, 'Santiago, Chile')

if __name__ == "__main__" :
	unittest.main()