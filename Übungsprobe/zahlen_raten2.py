from random import randint

def to_int(value):
    try:
        return int(value)
    except:
         return -1


def is_valid(value):
    if value < 0 or value > 100:
        return False
    return True
    

def abfrage(round):
    valid = False
    while not valid:
        rawinput = input(f'{round}. Versuch: Gib eine ganze Zahl zwischen 0 und 100 ein: ')
        int = to_int(rawinput)
        valid = is_valid(int)
    return int
    

def play():
    number = randint(0,100)
    round = 1
    geraten =-1
    while geraten != number:
        geraten = abfrage(round)
        round = round + 1
        if geraten > number:
            print('Die eingegebene Zahl ist zu gross')
        elif geraten < number:
            print('Die eingegebene Zahl ist zu klein')
    print(f'Bravo, du hast in {round} Runden die gesuchte Zahl {number} gefunden.')

play()