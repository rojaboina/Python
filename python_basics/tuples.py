#creating tuples
menu=('dosa','idli','puri','upma')
for food in menu:
 print(food)
 #throws error because tuples cannot be reassigned
menu[0]='pongal'
print(menu)

