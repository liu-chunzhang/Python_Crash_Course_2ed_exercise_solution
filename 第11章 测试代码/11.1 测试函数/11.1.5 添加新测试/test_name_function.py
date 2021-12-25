import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	""" 测试name_function.py。 """

	def test_first_last_name(self):
		""" 能够正确地处理像Janis Joplin这样的姓名吗？ """
		formmatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formmatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		""" 能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？ """
		formmatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formmatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__' :
	unittest.main()