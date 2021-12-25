from random import randint

class Die:

	# Die类的构造函数。
	def __init__(self, sides=6):
		self.sides = sides

	# 投骰子的函数。
	def roll_die(self):
		print(randint(1,self.sides))

def roll_die_10_times(die):
	for cycnum in range(0, 10):
		die.roll_die()
	print()