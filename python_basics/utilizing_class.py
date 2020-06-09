from Restaurent import *

restaurent = Restaurent('paradise','indian')
print(restaurent.restaurent_name)
print(restaurent.cusine_type)

restaurent1 = Restaurent('kobe','thai')
print(restaurent.restaurent_name)
print(restaurent.cusine_type)

restaurent1.describe_restaurent()
restaurent1.open_restaurent()