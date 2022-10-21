from ast import Num
from dataclasses import field
from random import*

# 5*5 Field

Row = 5
Coloumns = 5

field = []

for m in range(Row):
    field.append([])
    for n in range(Coloumns):
        Num = 2**(randint(0,5))
        field[m].append(Num)

#print('A  B  C  D  E')
#print('+--+--+--+--+')

#print('1|')

line = '+-----+-----+-----+-----+-----+'
midline = ['|    |    |    |    |    |']

for i in range(Row):
    print(line)
    for j in range(Coloumns):
        if field[i][j] == 16 or 32 or 64:
            len = '  '
        else:
            len = '   '
        print(f'| ',field[i][j], end=len)
    print('|')
print(line)
