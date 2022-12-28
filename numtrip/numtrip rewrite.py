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
        Num = 2**(randint(0,6))
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
    print('')

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
    inpx = input(Questionx)[0]
    while not inpx in '01234':
        print('input not valid')
        inpx = input(Questionx)
    numx=int(inpx)
    return numx

def Y_Inputcheck(Questiony):
    inpy = input(Questiony)[0]
    while not inpy in '01234':
        print('input not valid')
        inpy = input(Questiony)
    numy=int(inpy)
    return numy

adjlist = []
lenlist = len(adjlist)
def checkadj(x,y):
    left = (x > 0 and field[y][x] == field[y][x - 1]) or False #expressions to make life easier
    right = (x < 4 and field[y][x] == field[y][x + 1]) or False
    up = (y > 0 and field[y][x] == field[y - 1][x]) or False
    down = (y < 4 and field[y][x] == field[y + 1][x]) or False
    anyadj = left or right or up or down
    
    
    if not anyadj and (y!=oldy or x!=oldx): #if you advance into some field, and around this field nothing is same, it should return to original field
        field[y][x] = 0
        y=oldy
        x=oldx

    elif not anyadj: #stop if there's nothing in the first place
        return False

    else:
        if down:
            adjlist.append([y+1,x])
            field[y][x] = 0
            checkadj(x,y+1)
        if up:
            adjlist.append([y-1,x])
            field[y][x] = 0
            checkadj(x,y-1)
        if left:
            adjlist.append([y,x-1])
            field[y][x] = 0
            checkadj(x-1,y)
        if right:
            adjlist.append([y,x+1])
            field[y][x] = 0
            checkadj(x+1,y)
        
    
  
def checkdel_and_double():
    if checkadj(x,y) is True:
        for i in range(lenlist):
            field[adjlist[i][0]][adjlist[i][1]] = 0
        field[oldy][oldx] = 2*oldfield

    

def replacetop():        
    if field[0][x] == 0:
        field[0][x] == 2**(randint(0,6))

def giveup():
    global roundcount
    if not roundcount == 0:
        give_up = input('Continue (y), or give up (n)?')
        if give_up in 'nN':
            print(f'You gave up in round {roundcount}')
            return True
        else:
            return False
    else:
        return False



while giveup() is False:
    playground()
    x = X_Inputcheck('X Axis:')
    y = Y_Inputcheck('Y Axis:')
    oldx = x
    oldy = y
    oldfield = field[y][x]
    print(f'You the chose field with the number', field[y][x])
    checkdel_and_double()
    adjlist.clear()
    roundcount+=1

    