#print numbers 1 to 20
for value in range(1,21):
 print(value) #indentation after :

 #4-4 one to one million
 #values = list(range(1,1000001))
 #print(values)
 #print(max(values))
 #print(min(values))
 #print(sum(values))

numbers = [i for i in range(1,1000001)]
print(min(numbers)) #i have questions, i don't understand this
print(max(numbers))
print(sum(numbers))



for value in range(1,21,2):
 print(value)