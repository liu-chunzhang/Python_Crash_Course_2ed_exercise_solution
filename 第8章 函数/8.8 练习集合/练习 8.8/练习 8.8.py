def make_album(singer_name, album_name, songnumber=None):
	if songnumber:
		return {'singername': singer_name, 'albumname': album_name, 'songnumbers': songnumber}
	else :
		return {'singername': singer_name, 'albumname': album_name}

def continuedetermine():
	flag = input("If you want to note some information about singers and their albums? (yes/no) ")
	if flag == 'no' :
		return False
	else :
		return True

flag = continuedetermine()

while flag:
	singer_name = input("Please input the name of singer. ").title()
	album_name = input("Please input the name of one of his(her) albums: ")
	songnumber = input("And if you want to input the number of songs? (yes/no) ")
	if songnumber == 'no':
		message = make_album(singer_name, album_name)
	else :
		songnumber = input("Please input the number of this album. ")
		message = make_album(singer_name,album_name,songnumber)
	print(message)
	flag = continuedetermine()