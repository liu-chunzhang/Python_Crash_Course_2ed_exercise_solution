def describe_pet2(pet_name, animal_type = 'dog'):
	""" 显示宠物的信息。 """
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

# 一条名为Willie的小狗。
describe_pet2('willie')
describe_pet2(pet_name='willie')

# 一只名为Harry的仓鼠。
describe_pet2('harry', 'hamster')
describe_pet2(pet_name='harry', animal_type='hamster')
describe_pet2(animal_type='hamster', pet_name='harry')