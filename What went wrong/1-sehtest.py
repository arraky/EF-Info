'''
Probe EF 2022
Programm 1-SEHTEST.PY


Probe EF 2022
Programm 1-SEHTEST.PY



Ergebnis = []
'''

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def Wall_left():
    print('* *')

def Wall_bothsides(size):
    print('* * ', end=' ')
    for i in range(size+2):
        print(' ',end='')
    print('* *')

def Wall_right(size):
    for i in range(size+2):
        print('  ',end='')
    print('* *')

def Floor(size):
    for i in range(2):
        for i in range(4+size):
            print('* ', end='')
        print('')
    
def c(size, Direction):
    if Direction == 'U' or 'u':
        Wall_bothsides(size)
        Floor(size)
    elif Direction == 'R' or 'r':
        Floor(size)
        Wall_left()
        Floor(size)
    elif Direction == 'L' or 'l':
        Floor(size)
        for i in range(size):
            Wall_right(size)
        Floor(size)
    elif Direction == 'D' or 'd':
        Floor(size)
        for i in range(size+2):
            Wall_bothsides(size)


Eingabe = input('Eingabe: ')
Sizeinp = Eingabe[0]
Rotinp = Eingabe[1]


while not Rotinp == 'R' or 'r' or 'U' or 'u' or 'L' or 'l' or 'D' or 'd':
    Eingabe = input('not valid; Eingabe: ')
    Sizeinp = Eingabe[0]
    Rotinp = Eingabe[1]

    
while not is_integer_num(Sizeinp):
    Eingabe = input('not valid; Eingabe: ')   






    
    

