def make_album(singer_name, album_name, songnumber=None):
	if songnumber:
		return {'singername': singer_name, 'albumname': album_name, 'songnumbers': songnumber}
	else :
		return {'singername': singer_name, 'albumname': album_name}

message = make_album('Aimer', 'Torches ', 5)
print(message)

message = make_album('Aimer', '春はゆく / marie ')
print(message)

message = make_album('Sora Amamiya', 'Skyreach')
print(message)