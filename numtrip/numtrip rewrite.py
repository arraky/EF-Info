from ast import Num
from dataclasses import field
from random import*

# 5*5 Field
Row = 5
Coloumns = 5
roundcount = 0

field = []

#Give field[] random 2^randint
for m in range(Row):
    field.append([])
    for n in range(Coloumns):
        Num = 2**(randint(0,3))
        field[m].append(Num)

def fieldnum():
    print('  ',end='')
    for i in range(Row):
        print('   ',i, end='  ')
    print('')

def line():
    print('  ', end='')
    for i in range(Row):
        print('+------',end='')
    print('+')

def playground():
    fieldnum()
    for i in range(Row):
        line()
        print(i,end=' ')
        try:
            for j in range(Coloumns):
                if field[i][j] >=10:
                    len = ' '
                else:
                    len = '  '
                if field[i][j] >=100:
                    len = ''
                print(f'|  ',field[i][j], end=len)
            
        except:
            print(f'|  ',field[i][j], end='  ')
        print('|')
    line()

def X_Inputcheck(Questionx):
    inpx = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questionx))) 
    #Lambda defines a function here: Filter out everything that's not in '0123456789-'
    while len(inpx)!=1 or inpx not in '01234': #len(inpx) must be 1. if not, inputs like '01' or '012' would be allowed
        print('input not valid')
        inpx = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questionx)))
    numx=int(inpx)
    return numx

def Y_Inputcheck(Questiony):
    inpy = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questiony)))
    while len(inpy)!=1 or inpy not in '01234':
        print('input not valid')
        inpy = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questiony)))
    numy=int(inpy)
    return numy

adjlist = []
def checkadj(x,y,oldx,oldy):
    left = (x > 0 and field[y][x] == field[y][x - 1]) or False #expressions to make life easier
    right = (x < 4 and field[y][x] == field[y][x + 1]) or False
    up = (y > 0 and field[y][x] == field[y - 1][x]) or False
    down = (y < 4 and field[y][x] == field[y + 1][x]) or False
    anyadj = left or right or up or down

    
    if not anyadj and (y!=oldy or x!=oldx): #if you advance into some field, and around this field nothing is same, it should return to original field
        field[y][x] = 0
        y,x = oldy,oldx
        
    elif not anyadj: #stop if there's nothing in the first place
        return False

    else:
        if down:
            adjlist.append([y+1,x])
            field[y][x] = 0
            checkadj(x,y+1,oldy,oldx)
        if left:
            adjlist.append([y,x-1])
            field[y][x] = 0
            checkadj(x-1,y,oldy,oldx)
        if right:
            adjlist.append([y,x+1])
            field[y][x] = 0
            checkadj(x+1,y,oldy,oldx)
        if up:
            adjlist.append([y-1,x])
            field[y][x] = 0
            checkadj(x,y-1,oldy,oldx)
        return True

def checkdel_and_double():
    if checkadj(x,y, oldy,oldx) is True:
        field[oldy][oldx] = 2*oldfield
    
def replacetop():
    adjlist.sort()
    for i in range(len(adjlist)):
        dy = adjlist[i][0]
        dx = adjlist[i][1]
        while dy != 0:
            field[dy][dx] = field[dy-1][dx]
            field[dy-1][dx] = 0
            dy-=1
        field[0][dx] = 2**(randint(0,3))

def giveup():
    global roundcount
    if not roundcount == 0:
        give_up = input('Continue (y), or give up (n)?')
        if give_up in 'nN':
            print(f'You gave up in round: {roundcount}')
            return True
        else:
            return False
    else:
        return False

def endgameloss():
    global field
    endgameplayfield = [x[:] for x in field] #copies the whole field into endgameplayfield
    for i in range(5):
        for j in range(5):
            if checkadj(j,i, oldx=j, oldy=i) is True:
                field = [x[:] for x in endgameplayfield]
                adjlist.clear()
                return False #Continue Game
    print('Alas, you lost!')
    return True #Loss

def endgamewin():
    for i in range(5):
        for j in range(5):
            if field[i][j] == 256:
                return True#Win
            
while endgameloss() is False:
    if roundcount == 0: #show it the first time
        playground()
    else:
        pass

    x = X_Inputcheck('X Axis:') #Inputs
    y = Y_Inputcheck('Y Axis:')

    oldy,oldx = y,x #Stores values for later
    oldfield = field[y][x]

    print(f'You chose the field with the number:', field[y][x]) #Inform the player that the right field was chosen

    checkdel_and_double() #Recursion delete
    replacetop() #Fill up

    adjlist.clear() #Clear list, so it doesn't annoy us in the next round
    if endgamewin() is True: #Check if win condition is met; if so -> Congratulations
        print(f'You won! It took you {roundcount} rounds')
        break
    roundcount+=1 #counts the rounds
    print('New Field:')
    playground() #show the end result so that you can play again

    