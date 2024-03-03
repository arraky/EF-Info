from random import*

# 5*5 Field
Row = 5
Coloumns = 5
roundcount = 0

field = []

#Give field[] random 2^randint
for m in range(Row):
     field.append([])
     for n in range(Coloumns):
         Num = 2**(randint(0,3))
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
    print('+')

def playground():
    fieldnum()
    for i in range(Row):
        line()
        print(i,end=' ')
        for j in range(Coloumns):
            if 100>field[i][j] >10:
                print(f'| ',field[i][j], end='  ')
            elif 1000>field[i][j] >100:
                print(f'| ',field[i][j], end=' ')
            else:
                print(f'|  ',field[i][j], end='  ')
            
        print('|')
    line()

def Inputcheck(Question):
    inp = "".join(filter(lambda x: x in ['0','1','2','3','4','-'],input(Question))) 
    #Lambda defines a function here: Filter out everything that's not in '0123456789-'
    while len(inp)!=1: #len(inp) must be 1. if not, inputs like '01' or '012' would be allowed
        print('input not valid')
        inp = "".join(filter(lambda x: x in ['0','1','2','3','4','-'],input(Question)))
    num=int(inp)
    return num


adjlist = []
def checkadj(x,y,oldy,oldx):
    left = (x > 0 and field[y][x] == field[y][x - 1] and field[y][x]!=0) or False #expressions to make life easier
    right = (x < 4 and field[y][x] == field[y][x + 1] and field[y][x]!=0) or False # if x isn't bigger than 4 -> no out of bounds error
    up = (y > 0 and field[y][x] == field[y - 1][x] and field[y][x]!=0) or False #looks if field upwards is same as our current field
    down = (y < 4 and field[y][x] == field[y + 1][x] and field[y][x]!=0) or False #current field != 0, otherwise, in some cases there's going to be infinite loops (we don't like those)
    anyadj = left or right or up or down

    
    if not anyadj and (y!=oldy or x!=oldx): #if you advance into some field, and around this field nothing is same, it should return to original field
        field[y][x] = 0
        y,x = oldy,oldx
        
    elif not anyadj: #stop if there's nothing in the first place
        return False

    else:
        if down:
            adjlist.append([y+1,x]) #append element to adjlist
            field[y][x] = 0 #set current field to 0 -> no infinite loops
            checkadj(x,y+1,oldy,oldx) #repeat whole function at the element we added to adjlist
        if left:
            adjlist.append([y,x-1])
            field[y][x] = 0
            checkadj(x-1,y,oldy,oldx)
        if right:
            adjlist.append([y,x+1])
            field[y][x] = 0
            checkadj(x+1,y,oldy,oldx)
        if up:
            adjlist.append([y-1,x])
            field[y][x] = 0
            checkadj(x,y-1,oldy,oldx)
        return True

def checkdel_and_double():
    if checkadj(x,y,oldy,oldx) is True:
        field[oldy][oldx] = 2*oldfield #doubles the value of our original field if checkadj() is True
    
def replacetop():
    adjlist.sort() #sorts the list -> prevents errors
    for i in range(len(adjlist)):
        dy = adjlist[i][0] #easy life expressions
        dx = adjlist[i][1]
        while dy != 0:
            field[dy][dx] = field[dy-1][dx]
            field[dy-1][dx] = 0
            dy-=1 #go up one field
        field[0][dx] = 2**(randint(0,3)) #fill up the field at the top with a new number

def giveup(): #function obsolete, will keep it in case I want to use it later
    global roundcount
    if not roundcount == 0:
        give_up = input('Continue (y), or give up (n)?')
        if give_up in 'nN':
            print(f'You gave up in round: {roundcount}')
            return True
        else:
            return False
    else:
        return False

def endgameloss():
    global field
    endgameplayfield = [x[:] for x in field] #copies the whole field into endgameplayfield as a backup copy
    for i in range(5):
        for j in range(5):
            if checkadj(j,i, oldx=j, oldy=i) is True:
                field = [x[:] for x in endgameplayfield] #copy every element back
                adjlist.clear() #clear list so it doesn't affect the actual game
                return False #Continue Game
    playground()
    print(f'Alas, you lost! You lasted {roundcount} rounds')
    return True #Loss

def endgamewin():
    for i in range(5):
        for j in range(5):
            if field[i][j] == 256: #if any field has the value 256, it's a win
                return True#Win
            
while endgameloss() is False:
    if roundcount == 0: #show it the first time
        playground()
    else:
        pass

    x = Inputcheck('X Axis:') #Inputs
    y = Inputcheck('Y Axis:')

    oldy,oldx = y,x #Stores values for later
    oldfield = field[y][x]

    print(f'You chose the field with the number:', field[y][x]) #Inform the player that the right field was chosen

    checkdel_and_double() #Recursion delete
    replacetop() #Fill up

    adjlist.clear() #Clear list, so it doesn't annoy us in the next round
    if endgamewin(): #Check if win condition is met; if so -> Congratulations
        playground()
        print(f'You won! It took you {roundcount} rounds')
        break
    roundcount+=1 #counts the rounds
    print('New Field:')
    playground() #show the end result so that you can play again



