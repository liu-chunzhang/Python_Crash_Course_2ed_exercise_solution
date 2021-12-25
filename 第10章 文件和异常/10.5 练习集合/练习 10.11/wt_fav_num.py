import json

nums = []
while True:
	number = input("Please input your favorite number: ")
	nums.append(str(number))
	flag = input("If you want to input other numbers?(yes/no) ")
	if flag == 'no' :
		break
print(nums)

try:
	filename = 'favorite_numbers.json'
	with open(filename,'a') as fn :
		json.dump(nums,fn)
except FileNotFoundError:
	pass