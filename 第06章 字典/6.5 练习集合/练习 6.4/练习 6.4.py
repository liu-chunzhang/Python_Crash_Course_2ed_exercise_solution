# 一个用于打印字典结果的函数
def mapprint(amap):
	for term, term_value in amap.items():
		print(f"{term.title()}\n\t{term_value}.")

# 练习 6.3的代码块
terms = {
	'map': 'a data associative structure',
	"list": 'a data sequential structure',
	'if-else': 'a branch structure',
	'sublime text3':'a software for some advanced programming languages',
	'remove': 'a general function for some data structures'
	}

mapprint(terms)
print("\n\n")

# 接下来添加新的5个Python术语，之后打印。

terms['tuple'] = "a data sequential structure for constants"
terms['for'] = 'a loop structure'
terms['float'] = 'a type of data'
terms['int'] = 'a type of data'
terms['range'] = 'a function for generating natural numbers'

mapprint(terms)