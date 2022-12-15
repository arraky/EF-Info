from random import randint


gesucht = randint(0, 100)



def abfrage_to_int(runde):
    while not geraten.isnumeric():
        print('Eingabe nicht valide')
        geraten= input(f'{runde}. Versuch: Gib eine ganze Zahl zwischen 0 und 100 ein: ')
            
    int(geraten)
    return geraten

def play(geraten, runde):
    while geraten != gesucht:
        abfrage_to_int(runde=1)
        runde = runde + 1
        if geraten > gesucht:
            print('Die eingegebene Zahl ist zu gross')
        elif geraten < gesucht:
            print('Die eingegebene Zahl ist zu klein')
    print(f'Bravo, du hast in {runde} Runden die gesuchte Zahl {gesucht} gefunden.')

play(geraten=-1,runde=1)


