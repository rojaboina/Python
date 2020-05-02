
pets=[]
#creating a dictionary
pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)
#creating a dictionary
pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

#printing the entire dictionary through lists
for animals in pets:
	print(animals['name'].title())
for key,value in pet.items():
	print(key,str(value))  #why is it printing only one for me