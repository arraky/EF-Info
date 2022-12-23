from ast import Num
from dataclasses import field
from random import*

# 5*5 Field

Row = 5
Coloumns = 5

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

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

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



def checkadj(x,y):
    not_left = (x > 0 and field[y][x] != field[y][x - 1]) or False
    not_right = (x < 4 and field[y][x] != field[y][x + 1]) or False
    not_up = (y > 0 and field[y][x] != field[y - 1][x]) or False
    not_down = (y < 4 and field[y][x] != field[y + 1][x]) or False
    noadj = not_left and not_right and not_up and not_down

    if noadj and (y!=oldy or x!=oldx): #
        field[y][x] = 0
        y=oldy
        x=oldx

    elif noadj:
        return False

    
    else:
        if not not_down:
            field[y][x] = 0
            y+=1
            checkadj(x,y)
            return True
        
        elif not not_up:
            field[y][x] = 0
            y-=1
            checkadj(x,y)
            return True
                
        elif not not_right:
            field[y][x] = 0
            x+=1
            checkadj(x,y)
            return True
                
        elif not not_down:
            field[y][x] = 0
            x-=1
            checkadj(x,y)
            return True
        
        else:
            return False
    
  
def checkdel_and_double():
    if checkadj(x,y) is True:
        field[y][x] = 2*oldfield
        return True
    

def replacetop():
    if field[0][x] == 0:
        field[0][x] == 2**(randint(0,6))

def endgame():
    for x in range(4):
        for y in range(4):
            if field[y][x] != field[y+1][x] or y!=4 and y!=0 or field[y-1][x] and field[y][x+1] or x!=4 and field[y][x-1] or x!=0:
                return True


for i in range(5):
    playground()
    x = X_Inputcheck('X Axis:')
    y = Y_Inputcheck('Y Axis:')
    oldx = x
    oldy = y
    oldfield = field[y][x]
    print(f'You the chose field with the number', field[y][x])
    checkdel_and_double()
    
    