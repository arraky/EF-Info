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
    inpx = input(Questionx)
    while not is_integer(inpx):
        print('input not valid')
        inpx = input(Questionx)
    numx=int(inpx)
    while numx < 0 or numx>4:
        print('number not valid')
        inpx = input(Questionx)
        numx=int(inpx)
    return numx

def Y_Inputcheck(Questiony):
    inpy = input(Questiony)
    while not is_integer(inpy):
        print('input not valid')
        inpy = input(Questiony)
    numy=int(inpy)
    while numy < 0 or numy>4:
        print('number not valid')
        inpy = input(Questiony)
        numy=int(inpy)
    return numy

    not_left = (x > 0 and field[y][x] != field[y][x - 1]) or False
    not_right = (x < 4 and field[y][x] != field[y][x + 1]) or False
    not_up = (y > 0 and field[y][x] != field[y - 1][x]) or False
    not_down = (y < 4 and field[y][x] != field[y + 1][x]) or False
    noadj = not_left and not_right and not_up and not_down

    if noadj and (y!=oldy or x!=oldx):
        field[y][x] = 0
        y=oldy
        x=oldx

    elif noadj:
        return False
                
            if field[y][x+1] == field[y][x+1]:
                field[y][x+1] == 0
                checkadj(x+1,y)
               
            if field[y][x-1] == field[y][x-1]:
                field[y][x-1] == 0
                checkadj(x-1,y)
            return True
    def checkanddel():
        try:
            checkadj()
        except:
            return False
    if checkadj(x,y) is True:
        field[x][y] *= 2
        return True


def replacetop():
    x = numx
    y = numy
    if field[0][x] == '':
        field[0][x] == 2**(randint(0,6))


for i in range(5):
    playground()
    numx = X_Inputcheck('X Axis:')
    numy = Y_Inputcheck('Y Axis:')
    print(field[numy][numx])
    checkdel_and_double()
    
    