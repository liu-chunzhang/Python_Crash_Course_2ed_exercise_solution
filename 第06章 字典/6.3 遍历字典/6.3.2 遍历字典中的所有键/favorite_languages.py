favorite_langeages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in favorite_langeages.keys():
	print(name.title())

print()

for name in favorite_langeages:
	print(name.title())

print()

friends = ['phil', 'sarah']
for name in favorite_langeages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		langeage = favorite_langeages[name].title()
		print(f"\t{name.title()}, I see you love {langeage}.")

if 'erin' not in favorite_langeages.keys():
	print("Erin, please take our poll!")