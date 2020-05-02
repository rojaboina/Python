#building a dictionary and looping the list through it
favourite_languages={
	'Roja':'Python',
	'Arun':'sales force',
	'Kyathi':'RPA',
	'Aadhya':'Arts'
}

for names,languages in favourite_languages.items():
	print(names.title() + " 's favourite language is " + languages.title())

print("\n")

coders=['Arun','Kyathi','david','becca','Adhya','beks']
for coder in coders:
	if coder in favourite_languages.keys():
		print(f"{coder} took the poll")
	else:
		print(f"{coder} took the poll")