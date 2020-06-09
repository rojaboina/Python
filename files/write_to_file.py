filename="name.txt"
with open(filename,'w') as file_object:
	name=input("please enter you name")
	file_object.write(name)
	