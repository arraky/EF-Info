board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

for zeile in board:
    for zelle in zeile:
        print(' -', end='') #Nach jeder Zeile gibt es eine Zeile "- - - - -", "end=''" macht, das nach jedem " -" ein weiterer Abstand kommt 
    print(' ')
    for zelle in zeile:
        print(f'|{zelle}', end='') #f'{Zelle} nimmt den Wert der Zelle ?, | macht die Abstände
    print('|') #Schluss der Zeile

for zelle in board[0]:
    print(' -', end='')
print(' ')