'''
Probe EF 2022
Programm 1-SEHTEST.PY


Probe EF 2022
Programm 1-SEHTEST.PY



Ergebnis = []
'''

def Wall_left():
    print('* *')

def Wall_bothsides(size):
    print('* *', end=' ')
    for i in range(size):
        print('  ',end='')
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
    if Direction in 'Uu':
        for i in range(size+2):
            Wall_bothsides(size)
        Floor(size)
    elif Direction in 'Rr':
        Floor(size)
        for i in range(size):
            Wall_left()
        Floor(size)
    elif Direction in 'Ll':
        Floor(size)
        for i in range(size):
            Wall_right(size)
        Floor(size)
    elif Direction in 'Dd':
        Floor(size)
        for i in range(size+2):
            Wall_bothsides(size)


Eingabe = input('Eingabe: ')
Sizeinp = Eingabe[0]
Rotinp = Eingabe[1]



while not Rotinp in 'RrUuLlDd' and Sizeinp in '1234567890': #bro that's so much easier, fuck me....
    Eingabe = input('not valid; Eingabe: ')
    Sizeinp = Eingabe[0]
    Rotinp = Eingabe[1]

Sizeinp = int(Sizeinp)



c(Sizeinp, Rotinp)






    
    

