from ast import Num
from dataclasses import field
from random import*

roundcount = 0
field = []
def Row_Inputcheck(QuestionRow):
    inpraw = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(QuestionRow)))
    #Lambda defines a function here: Filter out everything that's not in '0123456789-'
    while len(inpraw)!=1 or inpraw not in '0123456789':
        print('input not valid')
        inpraw = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(QuestionRow)))
    numrow=int(inpraw)
    return numrow
def Col_Inputcheck(QuestionCol):
    inpcol = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(QuestionCol)))
    while len(inpcol)!=1 or inpcol not in '0123456789':
        print('input not valid')
        inpcol = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(QuestionCol)))
    numcol=int(inpcol)
    return numcol

Col = Col_Inputcheck('Number of coloumns(1-9):')
Row = Row_Inputcheck('Number of rows(1-9):')

#Give field[] random 2^randint

filternumberx = '0123456789'[:Col]
filternumbery = '0123456789'[:Row]
for m in range(Row):
    field.append([])
    for n in range(Col):
        Num = 2**(randint(0,3))
        field[m].append(Num)

def fieldnum():
    print('  ',end='')
    for i in range(Col):
        print('   ',i, end='  ')
    print('')

def line():
    print('  ', end='')
    for i in range(Col):
        print('+------',end='')
    print('+')

def playground():
    fieldnum()
    for i in range(Row):
        line()
        print(i,end=' ')
        try:
            for j in range(Col):
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
    while len(inpx)!=1 or inpx not in filternumberx:
        print('input not valid')
        inpx = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questionx)))
    numx=int(inpx)
    return numx

def Y_Inputcheck(Questiony):
    inpy = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questiony)))
    while len(inpy)!=1 or inpy not in filternumbery:
        print('input not valid')
        inpy = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questiony)))
    numy=int(inpy)
    return numy

adjlist = []
def checkadj(x,y,oldx,oldy):        
    left = (x > 0 and field[y][x] == field[y][x - 1] and field[y][x]!=0) or False #expressions to make life easier
    right = (x < Col-1 and field[y][x] == field[y][x + 1] and field[y][x]!=0) or False
    up = (y > 0 and field[y][x] == field[y - 1][x] and field[y][x]!=0) or False
    down = (y < Row-1 and field[y][x] == field[y + 1][x] and field[y][x]!=0) or False
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
            checkadj(x,y+1,oldx,oldy)
        if left:
            adjlist.append([y,x-1])
            field[y][x] = 0
            checkadj(x-1,y,oldx,oldy)
        if right:
            adjlist.append([y,x+1])
            field[y][x] = 0
            checkadj(x+1,y,oldx,oldy)
        if up:
            adjlist.append([y-1,x])
            field[y][x] = 0
            checkadj(x,y-1,oldx,oldy)
        return True
        
def checkdel_and_double():
    if checkadj(x,y,oldx,oldy) is True:
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
    endgameplayfield = [x[:] for x in field]
    for i in range(Row):
        for j in range(Col):
            if checkadj(j,i, oldx=j, oldy=i) is True:
                field = [x[:] for x in endgameplayfield]
                adjlist.clear()
                return False #Continue Game
    print(f'Alas, you lost! You lasted {roundcount} rounds')
    return True #Loss

def endgamewin():
    for i in range(Row):
        for j in range(Col):
            if field[i][j] == 256:
                return True#Win
            

while endgameloss() is False:
    if roundcount == 0:
        playground()
    else:
        pass

    x = X_Inputcheck('X Axis:')
    y = Y_Inputcheck('Y Axis:')

    oldy,oldx = y,x
    oldfield = field[y][x]

    print(f'You chose the field with the number:', field[y][x])

    checkdel_and_double()
    replacetop()

    adjlist.clear()
    if endgamewin() is True:
        print(f'You won! It took you {roundcount} rounds')
        break
    roundcount+=1
    print('New Field:')
    playground() #show the end result so that you can ask to give up

    