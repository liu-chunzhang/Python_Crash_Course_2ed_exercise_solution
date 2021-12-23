def make_shirt(size='large', words='I love Python') :
	print(f'The size of T-shrit is {size} and the T-shirt is printed with "{words}".')

# 8.4(1)的要求：制作一件印有默认字样的大号T恤。
make_shirt()

# 8.4(2)的要求：制作一件印有默认字样的中号T恤。
make_shirt(size='middle')

# 8.4(3)的要求：制作一件印有其他字样的T恤。
make_shirt(words='Maxwell equations')