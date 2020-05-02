#creating a dictonary inside a dictionary
cities={
'toronto':{
	'country':'canada',
	'population':'200k',
	'fact':'too cold'
},
'queens':{
	'country':'canada',
	'population':'300k',
	'fact':'beautifull'
},
'montona':{
	'country':'canada',
	'population':'100k',
	'fact':'nice'
}
}
for key  , dictionary  in cities.items():
	print(f"country name is: {dictionary['country']}")

	#key is for the value cities and
	#dictionay is for all dictonaries inside