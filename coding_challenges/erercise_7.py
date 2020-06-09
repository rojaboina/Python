while True:
    player1= input("player1: Please enter your input")
    player2=input("playe2: please enter your input")
    
    
    if player1=='rock' and  player2=='scissors':
        print("player1 is winner")
        
    elif player1=='scissors' and player2=='paper':
        print("player1 is winner")
        
        
    elif player1=='paper' and player2=='rock':
        print("player1 is winner")
        
        
    else:
        print("player2 is winner")
