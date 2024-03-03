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
        print('    ',i, end=' ')
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

def checkdel_and_double():
    x = numx # x here: Row
    y = numy # y here: Coloumn
    def checkadjright():
        if y != 4 and field[x][y] == field[x][y+1]:
            field[x][y+1] = 0
            return True
        else:
            return False
    def checkadjleft():
        if y != 0 and field[x][y] == field[x][y-1]:
            field[x][y-1] = 0
            return True
        else:
            return False
    def checkadjup():
        if x !=4 and field[x][y] == field[x-1][y]:
            field[x-1][y] = 0
            return True
        else:
            return False
    def checkadjdown():
        if x !=0 and field[x][y] == field[x+1][y]:
            field[x+1][y] = 0
            return True
        else:
            return False
    def checkanddel():       
        try:
            checkadjup()
            checkadjdown()
            checkadjleft()
            checkadjright()
        except:
            return False
    if checkanddel() is True:
        field[x][y] *= 2
        return True
    

for i in range(5):
    playground()
    numy = X_Inputcheck('X Axis:')
    numx = Y_Inputcheck('Y Axis:')
    print(field[numx][numy])
    checkdel_and_double()
    