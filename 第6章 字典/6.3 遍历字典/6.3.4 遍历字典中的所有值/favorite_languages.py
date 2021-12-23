favorite_langeages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("The following langeages have been mentioned:")
for langeage in favorite_langeages.values():
	print(langeage.title())

print()

print("The following langeages have been mentioned:")
for langeage in set(favorite_langeages.values()):
	print(langeage.title())