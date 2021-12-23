favorite_langeages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil':['python','haskell']
	}

for name, langeages in favorite_langeages.items():
	print(f"\n{name.title()}'s favorite langeages are:")
	for langeage in langeages:
		print(f"\t{langeage.title()}")

# 教材中的程序的改进版本：若喜爱的语言一种和不止一种，所用的be动词形式应该不同，特此改进。
for name, langeages in favorite_langeages.items():
	if len(langeages) > 1 :
		temp = "are"
	elif len(langeages) == 1 :
		temp = 'is'
	print(f"\n{name.title()}'s favorite langeages {temp}:")
	for langeage in langeages:
		print(f"\t{langeage.title()}")