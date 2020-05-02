#lpassing list to dictionaries
information_person={'first_name':'Rose','last_name':'clooney','age':'25','city':'Hyderabad'}
print(information_person['first_name'])
print(information_person['last_name'])
print(information_person['age'])
print(information_person['city'])


#personal data
favourite_people={
'kya':'123',
'vad':'345',
'sara':'678'
}
people=favourite_people
print(f"{people}")

#or print like this
peoples=favourite_people['kya']
print("kya's favourite number is " + str(peoples) + ".")