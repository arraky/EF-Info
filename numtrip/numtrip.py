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

def midline():
    for i in range(Row):
        print('|')
    print('|')

def playground():
    fieldnum()
    for i in range(Row):
        line()
        print(i,end=' ')
        for j in range(Coloumns):
            if field[i][j] >=10:
                len = ' '
            else:
                len = '  '
            print(f'|  ',field[i][j], end=len)
        print('|')
    line()

playground()


def play():
    x = input('Welche Reihe?')
    y = input('Welche Zeile?')
    def check():
        if field[x][y] == field[x-1][y]:
            field[x-1][y] == ''
        if field[x][y] == field[x+1][y]:
            field[x+1][y] == ''
        if field[x][y] == field[x][y-1]:
            field[x][y-1] == ''
        if field[x][y] == field[x][y+1]:
            field[x][y+1] == ''
    check()

play()
    