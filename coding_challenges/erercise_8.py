import random

number1=random.randint(1,9)
number = int(number1)
guess=0
count=0

while guess !=number and guess != "exit":
    guess1=input("what's your guess")
    
    if guess1 == 'exit':
        break
    
    guess == int(guess1)
    count += 1
    
    if guess<number:
        print("smalll")
        
    elif guess==number:
        print("equal")
        
    else:
        print("greater")
    
    
    

    
    

    