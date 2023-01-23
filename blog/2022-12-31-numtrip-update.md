# Working game?
## Inputchecks
I removed the is_integer function and replaced it with a function in the X and Y Inputcheck:

    inpx = "".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questionx))) 

Lambda defines a function here: Filter out everything that's not in '0123456789-'

It then goes on about and checks if the input is in string '01234' and if the len(inpx) is 1. 
If that's not the case, it tells you to f*ck off.

jk 

It just tells you the input was invalid and the whole process starts anew.

## Chechadj()
It has a global adjacent list "adjlist". TBH I took this idea from Thomas (props to him). 

- The function now has 4 parameters instead of 2: x,y,oldx and oldy. Again, too fix "referenced before assignment errors"

- Instead of not_left, not_right etc. the functions now check if there is something instead of nothing -> 

        left = (x > 0 and field[y][x] == field[y][x - 1] and field[y][x]!=0) or False

- Now, most importantly, I got the recursion to work: E.g. If left, it appends this field to the adjlist, sets the current field to 0 and repeats the function on the square to the left

    ```py
    if left:
        adjlist.append([y,x-1])
        field[y][x] = 0
        checkadj(x-1,y,oldy,oldx)
    ```

## Replacetop()
- It takes the adjlist and sorts it at the beginning, so that it works from the top of the field downwards. This fixes some errors.
- I gave each element in the adjlist a name in a for loop:

        for i in range(len(adjlist)):
            dy = adjlist[i][0]
            dx = adjlist[i][1]
- The function takes the number from the field from above and puts it into field[dy][dx] and replaces this top field with 0. Dy is subtracted by 1 and the process begins again for the field that currently has a 0 in it. The moment it reaches the top, it gives this square a new number:

        while dy != 0:
            field[dy][dx] = field[dy-1][dx]
            field[dy-1][dx] = 0
            dy-=1
        field[0][dx] = 2**(randint(0,3))

## Giveup()
I provisorically created this function as a jump in for the lack of a working endgame() function. I may change it to a stop game function that saves the current playfield via JSON to another file. 

## Endgameloss()
This function checks on the whole field, if there's even a possible merge of fields. For this, I chose my function chechadj(x,y,oldx,oldy). To make it work, I had to create a new list "endgameplayfield", which copies the whole content of the playfield

    global field
    endgameplayfield = [x[:] for x in field]

Now in two for loops, it checks if Checkadj() is true. In checkadj() fields change their values though, so in the end, it copies those values back from the endgameplayfield

    for i in range(5):
        for j in range(5):
            if checkadj(j,i, oldx=j, oldy=i) is True:
                field = [x[:] for x in endgameplayfield]
                adjlist.clear()
                return False #Continue game
The return False tells my gameloop to continue. If there's no field to merge, you lost and it stops the loop and gives the player a game over message:

    print(f'Alas, you lost! You lasted {roundcount} rounds')
    return True #Loss

The roundcount is in the gameloop

## Endgamewin()
This function takes every value in the field and looks for the winning number, I set it to 256 for now. 

    for i in range(5):
        for j in range(5):
            if field[i][j] == 256:
                return True#Win

## Gameloop:

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
        print(f'You won! It took you {roundcount} rounds')
        break
    roundcount+=1 #counts the rounds
    print('New Field:')
    playground() #show the end result so that you can play again

I wrote the most important infos in it already. 

1.   It starts by showing the player the playground in round 0. 
2. Asks for inputs and stores those values for later.
3. I added a small print that shows the player the number in the field he chose.
4. Goes through the recursion and filling up functions
5. Clears the adjlist for the next roudn
6. Checks if you've won and shows the amount of rounds it took you
7. Adds 1 to the roundcount and shows the new field

## Game with variable field sizes
It's basically the same thing, I just replaced the hard written code (values like 4 and 5) with variables "Col" and "Row". At the beginning of the game, the player is asked for the size of the field. The input is checked through the same functions as X and Y_Inputcheck.

I must rewrite it though, as it currently allows for 1x1 fields which obviously don't work. And even other fields such as 1x5 tend to have no solution as it's all based on random (pseudorandom to be exact) numbers.
