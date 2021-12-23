# 6.3(1)的要求：想出前面学过的5个编程术语，将其用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
terms = {
	'map': 'a data associative structure',
	"list": 'a data sequential structure',
	'if-else': 'a branch structure',
	'sublime text3':'a software for some advanced programming languages',
	'remove': 'a general function for some data structures'
	}

# 6.3(2)的要求：以整洁的方式打印每个术语及其含义。
	# 先打印术语，在它后面加上一个冒号，再打印其含义。
for term in terms:
	print(f"{term.title()}: {terms[term]}.")

print()

	# 一行打印术语，再使用换行符(\n)插入一个空行，然后在下一行以缩进的方式打印其含义。
for term in terms:
	print(f"{term.title()}\n\t{terms[term]}.")