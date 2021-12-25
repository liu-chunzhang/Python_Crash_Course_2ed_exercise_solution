import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	""" 针对Employee类的测试。 """

	# 先使用setUp创建一个实例。
	def setUp(self):
		self.employee = Employee('Bob', 'David', 3000)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.annual_salary, 5000)

	def test_give_custom_raise(self):
		self.employee.give_raise(4500)
		self.assertEqual(self.employee.annual_salary, 4500)

if __name__ == "__main__" :
	unittest.main()