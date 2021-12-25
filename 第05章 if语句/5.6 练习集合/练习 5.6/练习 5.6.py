age = 23

if age < 2 :
	state = "infant"
elif age < 4 :
	state = "kid"
elif age < 13 :
	state = "child"
elif age < 20 :
	state = "adolescent"
elif age < 65 :
	state = 'adult'
else :
	state = "elder"



print(f"A man of {age} is in a state of {state}.")