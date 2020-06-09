def computepay(h,r):
    return h*r

def overtime(h,r):
	ot= (h-40)*(1.5*r)
	pay= ot + (40*r)
	return pay

hrs = input("Enter Hours:")
h=float(hrs)
rate= input("Enter pay")
r=float(rate)

#calling the function for 40 and below hours
if h<=40:
	p = computepay(10,20)
	print("Pay",p)

#calling the function for over 40 hours
elif h>40:
	over_time=overtime(45,10.5)
	print("Pay",over_time)




