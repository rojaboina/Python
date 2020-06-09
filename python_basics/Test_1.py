sandwhich_orders=['chicken','tuna','shrimp','fish']
finished_sandwhiches =[]
for sandwhich in sandwhich_orders:
	finished_sandwhiches=sandwhich_orders[:]
	print(f"the sandwhich that was made was {sandwhich}")
	#print(finished_sandwhiches)

i=1
while i<=3:
	i=i+1
	sandwhich_orders.append('pastrami')
print(sandwhich_orders)
for sandwhich in sandwhich_orders:
	if sandwhich == 'pastrami' :
		sandwhich_orders.remove('pastrami')
print("soryyyyy but pastrami ran out")
print(sandwhich_orders)
