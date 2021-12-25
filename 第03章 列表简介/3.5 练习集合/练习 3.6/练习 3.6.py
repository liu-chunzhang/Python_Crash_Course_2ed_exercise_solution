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

# 3.6(1)的要求：指明找到了更大的餐桌。
print("I have found a larger table.")

# 3.6(2)的要求：使用insert()将一位新嘉宾添加到名单开头。
names.insert(0,"Amy")

# 3.6(3)的要求：使用insert()将另一位新嘉宾添加到名单中间。
names.insert(2,'Bob')

# 3.6(4)的要求：使用append()将最后一位新嘉宾添加到名单末尾。
names.append('Hack')

# 3.6(5)的要求：向名单中的每位嘉宾发出邀请。
for name in names:
	print(f"I want you to invite to my party, {name.title()}.")