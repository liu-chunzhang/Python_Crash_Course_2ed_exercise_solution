# 创建文件流来源名。
filename = 'learning_python.txt'

# 第一次打印时读取整个文件。
with open(filename) as fn:
	content = fn.read()
print(content)

# 第二次打印时遍历文件对象。
with open(filename) as fn:
	for line in fn:
		print(line)

# 第三次打印时将各行存储在一个列表中，再在with代码块外打印他们。
with open(filename) as fn:
	lines = fn.readlines()
for line in lines:
	print(line)