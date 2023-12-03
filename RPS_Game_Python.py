import random

def gamewin(Computer, You):
    if Computer==You:
        return None
    
    elif Computer=='Rock':
        if You=='Scissor':
            return False
        elif You=='Paper':
            return True
        
    elif Computer=='Paper':
        if You=='Rock':
            return False
        elif You=='Scissor':
            return True
        
    elif Computer=='Scissor':
        if You=='Paper':
            return False
        elif You=='Rock':
            return True
        

print('Computer Turn: Rock or Paper or Scissor?\n')
randNo= random.randint(1,3)
if randNo==1:
    Computer='Rock'
elif randNo==2:
    Computer='Paper'
elif randNo==3:
    Computer='Scissor'

You = input('Your Turn: Rock or Paper or Scissor?\n')
a = gamewin(Computer, You)
print(f'Computer choose: {Computer}\n')
print(f'You Choose: {You}\n')

if a==None:
    print("The game is a TIE!")
elif a:
    print('YOU WIN!!')
else:
    print('YOU LOOSE!!')