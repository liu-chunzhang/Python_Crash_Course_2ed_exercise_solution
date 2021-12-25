place_names = []

while True:
	place_name = input("If you could visit one place in the world, where would you go? ")
	place_names.append(place_name)
	next_tip = input("And if you want to deliver another place? (Yes/No)")
	if next_tip == 'No' or next_tip == 'no' :
		break

print("The whole result of the research is:")
for place_name in set(place_names):
	print(place_name)