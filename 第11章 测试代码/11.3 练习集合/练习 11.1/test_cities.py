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