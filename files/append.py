filename="responses.txt"
with open(filename,'w') as file_object:
	while True:
		name=input("please tell me your name")
		response = input("why do you like programming")
		if name == 'quit':
			break
		else:
			file_object.write(f"{name} likes programming becuase {response} \n")
