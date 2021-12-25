import json

filename = 'favorite_numbers.json'
try:
	with open(filename) as fn :
		nums = json.load(fn)
except FileNotFoundError:
	num = input("Please input your favorite number, we will save it. ")
	with open(filename, 'w') as fn :
		nums = [num]
		json.dump(nums,fn)
		print(f"We will store {num}.")
else :
	for num in nums:
		print(f"We have stored {num}.")