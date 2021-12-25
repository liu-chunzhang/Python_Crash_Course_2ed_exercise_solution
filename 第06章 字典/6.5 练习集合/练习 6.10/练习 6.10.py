likenumbers = {
	'Amy': {3, 5, 8}, 
	'Bob': {6, 9, 13}, 
	'David': {7, 12}, 
	'Liu': {4}, 
	'Wu': {9, 10.7, 2}
	}

for man, nums in likenumbers.items():
	# 用变量message总领要总结的话。
	message = f"The favorite number of {man} "

	# 这一部分决定需要用的be动词。
	if len(nums) > 1 :
		beverb = "are"
	elif len(nums) == 1 :
		beverb = 'is'
	message += f"{beverb} "

	# 这一部分将所有的数字汇总到message中。
	while nums:
		temp = nums.pop()
		if len(nums) >= 1:
			message += f"{temp}, "
		else :
			message += f"{temp}."

	# 打出一条信息。
	print(message)