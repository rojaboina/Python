#copying from one list to another list

my_pizza=['chicken','panner','veggies']
friends_pizza=['beef','pork','ham']

#statement for copying
friends_pizza=my_pizza[:]
print(my_pizza)
print(friends_pizza)

print('\n')
my_pizza.append('cheese')
friends_pizza.append('goat')

print('\n')
print(my_pizza)
print(friends_pizza)

for food in my_pizza:
 print(food)