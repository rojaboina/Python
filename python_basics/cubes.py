#printing cubes exponentially
cubes=[]
for value in range(1,11):
 value=value**3
 cubes.append(value)
print(cubes)

#printing through list comprehension
squares=[value**3 for value in range(1,11)]
print(squares)

