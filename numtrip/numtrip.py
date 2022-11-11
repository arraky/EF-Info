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


#print('A  B  C  D  E')
def fieldnum():
    print('  ',end='')
    for i in range(Row):
        print(' ',i+1, end=' ')
    print('')
#print('+--+--+--+--+')
def line():
    print('  ',end='')
    for i in range(Row):
        for j in range(Coloumns):
            if field[i][j] >=10:
                lenstripe ='-'
            else:
                lenstripe ='--'
            print(lenstripe,end='')
        print('----',end='')
    print('')


#print('1|')
def midline():
    for i in range(Row):
        print('|')
    print('|')


def play():
    fieldnum()
    for i in range(Row):
        line()
        print(i,end=' ')
        for j in range(Coloumns):
            if field[i][j] >=10:
                len = ' '
            else:
                len = '  '
            print(f'|',field[i][j], end=len)
        print('|')
    line()

play()
