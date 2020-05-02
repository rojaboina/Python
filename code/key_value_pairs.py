#printing the key value pairs of dictionary
Rivers_dictionary={
	'Nile':'egypt',
	'Hindu':'India',
	'tungabadra':'INdia',
	'ganga':'India'
}

for River_name in Rivers_dictionary.keys():
	print(River_name.title())

for River_name in Rivers_dictionary.values():
	print(River_name.title())

for River_name,country in Rivers_dictionary.items():
	print(River_name.title(),"\n",country.title())

