![](./Top-Down-Picture/Top-Down.svg)
# Functions
## 1
```py
for m in range(Row):
     field.append([])
     for n in range(Coloumns):
         Num = 2**(randint(0,3))
         field[m].append(Num)
```
## 2
```py
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
```
## 3
```py
def replacetop():
    pass
    #function at header 11
```
## 4
```py
adjlist = []
def checkadj(x,y,oldy,oldx):
    pass
    #function at header 10

def checkdel_and_double():
    if checkadj(x,y,oldy,oldx) is True:
        field[oldy][oldx] = 2*oldfield #doubles the value of our original field if checkadj() is True
```
## 5
```py
while endgameloss() is False:
    if roundcount == 0: #show it the first time
        playground()
    else:
        pass

    x = X_Inputcheck('X Axis:') #Inputs
    y = Y_Inputcheck('Y Axis:')

    oldy,oldx = y,x #Stores values for later
    oldfield = field[y][x]

    print(f'You chose the field with the number:', field[y][x]) #Inform the player that the right field was chosen

    checkdel_and_double() #Recursion delete
    replacetop() #Fill up

    adjlist.clear() #Clear list, so it doesn't annoy us in the next round
    if endgamewin() is True: #Check if win condition is met; if so -> Congratulations
        playground()
        print(f'You won! It took you {roundcount} rounds')
        break
    roundcount+=1 #counts the rounds
    print('New Field:')
    playground() #show the end result so that you can play again
```
## 6
```py
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
```
## 7
```py
def X_Inputcheck(Questionx):
    inpx = "".join(filter(lambda x: x in ['0','1','2','3','4','-'],input(Questionx))) 
    #Lambda defines a function here: Filter out everything that's not in '0123456789-'
    while len(inpx)!=1: #len(inpx) must be 1. if not, inputs like '01' or '012' would be allowed
        print('input not valid')
        inpx = "".join(filter(lambda x: x in ['0','1','2','3','4','-'],input(Questionx)))
    numx=int(inpx)
    return numx

def Y_Inputcheck(Questiony):
    inpy = "".join(filter(lambda x: x in ['0','1','2','3','4','-'],input(Questiony)))
    while len(inpy)!=1:
        print('input not valid')
        inpy = "".join(filter(lambda x: x in ['0','1','2','3','4','-'],input(Questiony)))
    numy=int(inpy)
    return numy
```
## 8
```py
def playground():
    field[i][j] #this part in the playground function
```
## 9
```py
#This part in the gameloop:
    x = X_Inputcheck('X Axis:') #Inputs
    y = Y_Inputcheck('Y Axis:')

    oldy,oldx = y,x #Stores values for later
    oldfield = field[y][x]
```
## 10
```py
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
```
Takes the values as parameters in the function bracket
## 11
Takes the emptied field and refills it using the adjlist from the recursion algorithm
```py
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
```
## 12
```py
#this part in the gameloop
if endgamewin() is True: #Check if win condition is met; if so -> Congratulations
        playground()
        print(f'You won! It took you {roundcount} rounds')
        break
```
## 13
```py
#This part in the gameloop
print('New Field:')
playground() #show the end result so that you can play again
```
