rivernames = {
	"Nile": ["Rwanda", "Burudli", "Tanzania", "Kenya", "Uganda", "Zaire", "Sudan", "Ethiopia", "Egypt"],
	"Congo": ["Zambia", "Congo(Dr)", "Congo(Bravo)", "Angola"],
	"Mekong": ["China", "Laos", "Myanmar", "Thailand", "Cambolia", "Vietnam"]
	}

# 6.5(1)的要求：使用循环为每条河流打印一条消息。
for rivername in rivernames:
	message = f"The {rivername} flows through "
	for nationname in rivernames[rivername]:
		if( nationname != rivernames[rivername][-1] ) :
			message += f"{nationname}, "
		else :
			message += f"{nationname}."
	print(message)

# 6.5(2)的要求：使用循环将该字典的每条河流的名字打印出来。
for rivername in rivernames:
	print(rivername)

# 6.5(3)的要求：使用循环将该字典包含的每个国家的名字打印出来。
for nationnames in rivernames.values():
	temp = []
	for nationname in nationnames:
		temp.append(nationname)
	print(temp)