import random

# Snake water gun or Rock paper Scissors game
def gamewin(comp, Rohan):

    # If both choose same
    if comp == Rohan:
        return None
    
    # Check for all possibilities when the computer chose snake
    elif comp == 'S':
        if Rohan == 'W':
            return False
        elif Rohan =='G':
            return True

    # Check for all possibilities when the computer chose water 
    elif comp == 'W':
        if Rohan == 'G':
            return False
    elif comp == 'W':
        if Rohan == 'S':
            return True
        
    # Check for all possibilities when the computer chose gun
    elif comp =='G':
        if Rohan == 'S':
            return False
    elif comp == 'W':
        return True
    
print("Comp Turn: Snake(S) Water(W) or Gun(G)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'W'
elif randNo == 3:
    comp = 'G'

Rohan = input("Your Turn: Snake(S) Water(W) or Gun(G)?").upper()
A = gamewin(comp, Rohan)
print(f"Computer chose {comp}")
print(f"Rohan chose {Rohan}")

if A == None:
    print("The game is a tie!")
elif A == True:
    print("Rohan Wins!")
else:
    print("Rohan Loses!")        


              