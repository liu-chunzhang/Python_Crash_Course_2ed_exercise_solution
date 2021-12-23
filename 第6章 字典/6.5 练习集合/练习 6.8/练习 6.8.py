pet1 = {
	"name": "Killy",
	"kind": "cat",
	"master": "Amy"
}

pet2 = {
	"name": 'Joe',
	"kind": "dog",
	"master": "Bob"
}

pet3 = {
	"name": "Von",
	"kind": "gold fish",
	"master": "Wu"
}

pets = [pet1, pet2, pet3]

for pet in pets:
	for k, v in pet.items():
		print(f"{k}: {v}.")
	print()