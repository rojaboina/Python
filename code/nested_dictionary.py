#Appending a dictionary through list

people=[]
details1={
'jen':'mine',
'pen':'hive',
'when':'wow',
	}
people.append(details1)

details2={
	'joe':'nike',
	'peon':'mue',
	'ho':'pro',
}

people.append(details2)

for person in people:
	print(person)