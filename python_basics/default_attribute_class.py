class Restaurent:

	def __init__(self,restaurent_name,cusine_type):
		"  "  "   Initialize  variables " "  "
		self.restaurent_name=restaurent_name
		self.cusine_type=cusine_type
		self.number_served=0

	def describe_restaurent(self):
		msg=self.restaurent_name + "servers the delicious" + self.cusine_type
		print("\n"+msg)


	def open_restaurent(self):
		msg=self.restaurent_name + "is open during morning hours" 
		print("\n"+msg)

	def set_number_served(self,number_served):
		self.number_served=number_served
		print(f"number served  {number_served}")

	def increment_number_servered(self,additonal_number):
		 self.number_served += additonal_number
		 #print(f"number served  {number_served}")


a=Restaurent('Kobe','Thai')
a.describe_restaurent()
b=a.set_number_served(23)
c=a.increment_number_servered(433)
print(a.number_served)