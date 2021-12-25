diningnumber = int(input("How many people will you be dining with? "))
if diningnumber > 8 :
	message = "There are no vacant table now."
else :
	message = "There exist vacant tables now."
print(message)