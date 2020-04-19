my_pizza=['chicken','panner','veggies']
friends_pizza=['beef','pork','ham']
friends_pizza=my_pizza[:]
print(my_pizza)
print(friends_pizza)
my_pizza.append('cheese')
friends_pizza.append('goat')
print(my_pizza)
print(friends_pizza)
for food in my_pizza:
 print(food)