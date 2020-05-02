
#conditional statements.
sandwhich_orders=['chicken','tuna','shrimp','fish']
finished_sandwhiches =[]
for sandwhich in sandwhich_orders:
	finished_sandwhiches=sandwhich_orders[:]
	print(f"the sandwhich was made with {sandwhich}")
	#print(finished_sandwhiches)

#while loop
print("\n")
i=1
while i<=3:
	i=i+1
	sandwhich_orders.append('pastrami')
print(sandwhich_orders)


print("\n")
while 'pastrami' in sandwhich_orders:
		sandwhich_orders.remove('pastrami')
print("soryyyyy but pastrami ran out")
print(sandwhich_orders)
sandwhich_orders=['chicken','tuna','shrimp','fish']
finished_sandwhiches =[]
#for loop
for sandwhich in sandwhich_orders:
	finished_sandwhiches=sandwhich_orders[:]
	print(f"the sandwhich was made with {sandwhich}")
	#print(finished_sandwhiches)
print("\n")
i=1
while i<=3:
	i=i+1
	sandwhich_orders.append('pastrami')
print(sandwhich_orders)

print("\n")
for sandwhich in sandwhich_orders:
	if sandwhich == 'pastrami' :
		sandwhich_orders.remove('pastrami')
print("soryyyyy but pastrami ran out")
print(sandwhich_orders)
