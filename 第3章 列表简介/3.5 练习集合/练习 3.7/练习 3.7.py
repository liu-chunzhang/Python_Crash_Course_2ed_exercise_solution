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

# 练习 3.6的程序
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

# 3.7(1)的要求：打印一条只能邀请两位嘉宾共进晚餐的消息。
print("Now I can only invite two guests to dinner.")

# 3.7(2)的要求：使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
while len(names) > 2 :
	inviterName = names.pop()
	print(f"Sorry, {inviterName}. I am unable to invite you in my dinner.")

# 3.7(3)的要求：对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
for name in names:
	print(f"Please come to my dinner party on time, {names[-1]}.")

# 3.7(4)的要求：使用del将最后两位嘉宾从名单中删除。之后打印名单，核实程序结束时名单已变成空的。
while len(names) > 0 :
	del names[-1]
print(names)