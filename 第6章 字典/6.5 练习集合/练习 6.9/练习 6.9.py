favorite_places = {
	"Amy": ['Shanghai', 'Beijing', 'Guangzhou'],
	"Bob": ['Wuhan', 'Sichuan', 'Yunnan'],
	"Wu": ["Xizang", "Heilongjiang", "Xinjiang"]
}

for name in favorite_places:
	for placename in favorite_places[name]:
		print(f"{name} likes to go {placename}.")
	print()