class Restaurent:

	def __init__(self,restaurent_name,cusine_type):
		"  "  "   Initialize  variables " "  "
		self.restaurent_name=restaurent_name
		self.cusine_type=cusine_type

	def describe_restaurent(self):
		msg=self.restaurent_name + "servers the delicious" + self.cusine_type
		print("\n"+msg)


	def open_restaurent(self):
		msg=self.restaurent_name + "is open during morning hours" 
		print("\n"+msg)

restaurent = Restaurent('paradise','indian')
print(restaurent.restaurent_name)
print(restaurent.cusine_type)

restaurent.describe_restaurent()
restaurent.open_restaurent()