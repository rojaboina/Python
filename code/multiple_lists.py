current_users=['kyathi','arun','rose','raj','sara','swa']
new_users=['adhya','anvi','aanya','rose','kyathi']
for i in new_users:
	if i in current_users:
		print("user" + i + "has already been used")
	else:
    	print("This is" + i + "a new user")
#donno why it is not working