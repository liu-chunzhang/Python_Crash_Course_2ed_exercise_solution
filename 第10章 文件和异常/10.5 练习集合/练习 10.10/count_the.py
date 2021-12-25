try:
	filename = "little_women.txt"
	with open(filename) as lw:
		lines = lw.readlines()
		
except FileNotFoundError:
	print("The file you input doesn't exist.")
else:
	summary = 0
	for line in lines:
		line = line.lower()
		summary += line.count('the ')
	print(f"The total number of 'the' in input file {filename} is {summary}.")