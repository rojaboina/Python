
filename="assignment.txt"
with open(filename,'a') as file_object:
	while True:
		name=input("please enter you name")
		if name == 'quit':
			break
		else:
			print(f"hello{name}\n")
			file_object.write(f"you have assigned assignment to {name} ")
	

