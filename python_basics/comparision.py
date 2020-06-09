largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num=='done':
        break
    try:
        s=int(num)
        if largest==None:
            largest=s
        elif s>largest:
            largest=s

        if smallest==None:
            smallest=s
        elif s<smallest:
            smallest=s
    except:
        print('Invalid input')
        continue

print("Maximum is",largest)
print("Minimum is",smallest)