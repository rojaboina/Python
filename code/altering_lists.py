#Adding three people to your guest list and printing any message for them
List=["Adhya","Roja","kyathi","Arun","Raj","Nutyy","baby"]
a=List[0]
msg="hello" + "\t" + a
print(msg)
msg1=f"hello {List[1]}"
print(msg1)

#adding a new person through using append
List.append("priya")
print(List)

#Removing (using del) few guests since she can't make it and replacing it with someone else

del List[0] #using del function we need to mention the place from which the item needs to be deleted
print(List)

#oh i deleted a wrong person so let me add back

List.insert(0,'Aadhya')
print(List)

#We can use remove function if we don't know the postion but just the value
List.remove('Raj')
print(List)

#deleting using pop function
b=List.pop() #by default the last element is deleted and stored for further use
print(b)

#pop using position
b=List.pop(1)
print(b)


#inserting at the begging of your list
List.insert(3,'mona')
print(List)

#pop plus message
b=List.pop()
c= "sorry" + " " + b + " " + "we cannot invite you"
print(c)

