#passing the values through a list to check if they exist in a dictionary
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

#parsing the list first and then comparing if the values in list exist in dictonary
for coder in coders:
	if coder in favourite_languages.keys():
		print(f"{coder} took the poll")
	else:
		print(f"{coder} took the poll")