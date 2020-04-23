numbers=['1','2','3','4','5','6','7','8','9']
for i in numbers:
	if i in numbers:
		print(f"{i}st")
	else:
		print("no")

#using a range

numbers= list(range(1,11))
print(numbers)