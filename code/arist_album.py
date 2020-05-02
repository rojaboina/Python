#dictionaries through functions
def make_album(artist_name,album_title):
	person={'artist_name':artist_name,'album_title':album_title}
	return person
#if the return is removed this does not work
musician = make_album('Roja','Roja jane man')
print(musician)