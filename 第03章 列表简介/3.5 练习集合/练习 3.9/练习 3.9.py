# 使用练习 3.5的程序
# 练习 3.4的程序
names = [ 'Tim', 'Jack', 'Ben' ]

for name in names:
	print(f"I'd like to have dinner with you, {name.title()}.")

# 练习 3.5的程序
# 3.5(1)的要求：指出Ben已经不能来赴约。
print("Ben is unable to my party.")

# 3.5(2)的要求：修改嘉宾名单，将无法赴约的嘉宾姓名替换为新邀请的嘉宾的姓名。
names[2] = "David"

# 3.5(3)的要求：再次打印一系列消息，向名单中的每一位嘉宾发出邀请。
for name in names:
	print(f"I want you to invite to my party, {name.title()}.")

# 3.9的要求
print(f"I have invited {len(names)} people to my dinner.")