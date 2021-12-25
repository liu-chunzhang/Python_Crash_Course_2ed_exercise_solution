def count_words(filename):
	""" 计算一个文件大致包含多少个单词。 """
	try :
		with open(filename, encoding = 'utf-8') as f:
			contents = f.read()
	except FileNotFoundError :
		pass
	else :
		# 计算该文件大致包含多少个单词。
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)