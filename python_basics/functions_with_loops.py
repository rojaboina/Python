def make_album(artist_name,album_title):
""build a dictionary containing information""
	person={'artist_name':artist_name,
	'album_title':album_title}
	return person
	
#providing user to give inputs
name_prompt="enter your favourite artist input"
title="enter album name"

#letting user know how to quit
print("enter 'quit' to stop anytime")

while True:
#assigning values 
	artist_name=input(name_prompt)
	if artist_name=='quit':
		break

	album_title=input(title)
	if album_title=='quit':
		break
album=make_album(artist_name,album_title)
print(album)