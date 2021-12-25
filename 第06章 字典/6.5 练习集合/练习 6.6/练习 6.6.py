# 6.6(1)的要求：创建一个应该会接受调查的人员名单，其中有些人已经包含在字典中，而其他人未包含在字典中。
allnames = {'jen', 'sarah', 'edward', 'phil'}
passednames = {'sarah', 'edward'}

# 6.6(2)的要求：遍历这个人员名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条消息邀请他参加。
for name in allnames:
	if name in passednames:
		print(f"{name.title()}, thanks for your help.")
	else:
		print(f"{name.title()}, please join our research.")