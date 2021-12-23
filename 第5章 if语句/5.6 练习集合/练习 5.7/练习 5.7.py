# 5.7(1)的要求：创造一个包含三种水果名称的列表。
favorite_fruits = ['apple', 'pear', 'peach']

# 为简单，编写一个辅助函数。
def fruitprint(fruitname):
	print(f"You really like {fruitname}s!")

if 'banana' in favorite_fruits:
	fruitprint('banana')
if 'apple' in favorite_fruits:
	fruitprint('apple')
if 'watermelon' in favorite_fruits:
	fruitprint('watermelon')
if 'pear' in favorite_fruits:
	fruitprint('pear')
if 'peach' in favorite_fruits:
	fruitprint('peach')