names = ['Amy', 'Bob', 'David', 'Tom', 'Zhou', 'Song']

# 访问元素
	# 不按照索引直接访问
print(names)

	# 按照索引访问
print(names[1])

print()

# 修改、添加和删除元素
	# 修改列表元素
		# 使用索引修改列表元素
names[2] = 'Jack'
print(names)

print()

	# 在列表中添加元素
		# 在列表末尾添加元素
names.append('Kin')
print(names)

print()

		# 在列表中插入元素
names.insert(2, 'John')
print(names)

print()

	# 从列表中删除元素
		# 使用del语句删除元素
del names[2]
print(names)

print()

		# 使用方法pop()删除元素
temp = names.pop()
print(names)
		
print()

		# 弹出列表中任何位置处的元素
temp = names.pop(-2)
print(names)

print()

		# 根据值删除元素
names.remove('Bob')
print(names)

print()

# 组织列表
	# 使用方法sort()对列表永久排序
temp = names[:]	# 这里必须传值而不能传址！语法辨析见教材P55-P56
names.sort()
print(names)

print()

	# 使用函数sorted()对列表临时排序
print(temp)
print(sorted(temp))
print(temp)

print()

	# 倒着打印列表
print(temp)
temp.reverse()
print(temp)

print()
	
	# 确定列表的长度
print(len(temp))