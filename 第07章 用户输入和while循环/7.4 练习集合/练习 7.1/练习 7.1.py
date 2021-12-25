carname = input("You can tell me what kind of cars do you like? ")
if carname == 'bmw':
	carname = carname.upper()
else :
	carname = carname.title()
print(f"Let me see if I can find you a {carname}.")