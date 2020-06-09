#Using the case functions and strip functions
Eric="Hello eric would you like to learn some python today?"
print(Eric);

a="Roja"
#converting the variable to lower case
print(a.lower());
#converting the variable to upper case
print(a.upper());
#converting the Variable to tile case
print(a.title());

famous_person=' "A person \n who never made a mistake never tried \n anything new " '
message = f"Albert Einstein once said,{famous_person}"
print(message);

famous_person=" A person \n who never made a mistake never tried \n anything new \" "
message ="Albert Einstein once said"
a= f"{message}, {famous_person} ";

person="\troja\n"
print(person);
#Removing the spaces on the left
print(person.lstrip());
#Removing the spaces on the right
print(person.rstrip());
#Removing the spaces on both sides
print(person.strip()); 
