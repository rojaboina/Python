
while True:
    num = input("Enter a number: ")
    if num == "done" : 
    	break
 
    try:
    	n=int(num)
    except:
    	print ("can't use string type")

def large_small():
	
	largest = None
	smallest=None

	if largest is None:
			largest=n
	elif largest<n:
			largest=n


	if smallest is None:
			smallest=n
	elif smallest>n:
			smallest=n
			
	print('largest number is:', largest)
	print('smallest number is:', smallest)


large_small()

