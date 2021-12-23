# 3.8(1)的要求：将这些地方存储在一个列表中，并确保其中的元素不是按照字母顺序排列的。
travel_sites = ['Beijing', 'Shanghai', 'Xian', 'Xizang', 'Guizhou']

# 3.8(2)的要求：按原始排列顺序打印该列表。
for site in travel_sites:
	print(site)

print() # 单纯为了结果清晰而添入的隔断语句，无实际意义。下同。

# 3.8(3)的要求：使用sorted()按字母顺序打印这个列表，同时不要修改它。
for site in sorted(travel_sites):
	print(site)

print()

# 3.8(4)的要求：再次打印该列表，核实排列顺序未变。
for site in travel_sites:
	print(site)

print()

# 3.8(5)的要求：使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。

for site in sorted(travel_sites, reverse = True) :
	print(site)

print()

# 3.8(6)的要求：再次打印该列表，核实排列顺序未变。
for site in travel_sites:
	print(site)

print()

# 3.8(7)的要求：使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
travel_sites.reverse()
for site in travel_sites:
	print(site)

print()

# 3.8(8)的要求：使用reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
travel_sites.reverse()
for site in travel_sites:
	print(site)

print()

# 3.8(9)的要求：使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
travel_sites.sort()
for site in travel_sites:
	print(site)

print()

# 3.8(10)的要求：使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
travel_sites.sort(reverse = True)
for site in travel_sites:
	print(site)