try:
	with open("cats.txt") as cats:
		catsline = cats.readlines()

	with open("dogs.txt") as dogs:
		dogsline = dogs.readlines()
		
except FileNotFoundError:
	pass

else:
	for cat in catsline:
			print(cat.rstrip())
	for dog in dogsline:
			print(dog.rstrip())