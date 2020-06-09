#while with elif statements
while True:
	age=input("Tell me your age")
	if int(age)<3:
		print("free")
	elif int(age)>3 and int(age)<12:
		print("$10 ticket")
	elif int(age)>12:
		print("$15")
	elif age == 'quit':
		break
