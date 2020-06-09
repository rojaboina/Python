#printing the list,values of dictionary
friends_dictonary={
	'kyathi':'Never lifts calls',
	'vadduri':'Never behaves',
	'Aadya':'Awesome',
	'Roja':'Never forgets to eat food'
}

for friend_names, activities in friends_dictonary.items():
	print(f"{friend_names}:{activities}")