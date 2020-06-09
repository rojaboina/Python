#dictionary inside a dictionary

pets=[]

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

for animals in pets:
	print(animals['name'].title())
for key,value in pet.items():
	print(key,str(value))  #why is it printing only one for me