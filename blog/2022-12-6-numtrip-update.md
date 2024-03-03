# Recursion
This is the theme of this blog entry

## New Functions

### Checkdel_and_double()
A small function to check if you should double the content of field[y][x]:
```py
    def checkdel_and_double():
        if checkadj(x,y) is True:
            field[y][x] = 2*oldfield
            return True
```
### Replacetop()
If the top field is emptied, it can't take numbers from above as their are no rows above it (obviously). Thus created a function (haven't implemented it yet) that creates new numbers similar to the random numbers filling up field[] at the beginning of the code
```py
    def replacetop():
        if field[0][x] == 0:
            field[0][x] == 2**(randint(0,6))
```
### Endgame()
Again a function that I haven't implemented yet. It's supposed to constantly check the whole field for a possible field to be marked.
```py
    def endgame():
        for x in range(4):
            for y in range(4):
                if field[y][x] != field[y+1][x] or y!=4 and y!=0 or field[y-1][x] and field[y][x+1] or x!=4 and field[y][x-1] or x!=0:
                    return True
```
### Is_integer(n):
Copied that from the internet. It checks if the input is a float or an integer. Needed it for X- and Y-Inputcheck, because otherwise the program crashed with inputs like '0.1'
```py
    def is_integer(n):
        try:
            float(n)
        except ValueError:
            return False
        else:
            return float(n).is_integer()
```
## Changes to checkadj(x,y)
Added parameters in paranthesis to account for error "referenced before assignment"

### Added a not_left, not_right etc.
statement with or False at the end so I could all put it into the statement "noadj"
```py
    not_left = (x > 0 and field[y][x] != field[y][x - 1]) or False
    not_right = (x < 4 and field[y][x] != field[y][x + 1]) or False
    not_up = (y > 0 and field[y][x] != field[y - 1][x]) or False
    not_down = (y < 4 and field[y][x] != field[y + 1][x]) or False
    noadj = not_left and not_right and not_up and not_down
```
### Added an if and elif statement
After you check the surroundings of field[y][x], say [y][x+1] and [y][x-1] have the same number in them. My code then empties [y][x] to allow for recursion (otherwise infinite loop between [y][x] and [y][x+1]) and goes to [y][x+1] to check this field's surroundings (Recursion). If it doesn't find anything new, it should return to the original y and x values to check at [y][x-1]. Thus I added this in my play loop: 
```py
    oldx = x
    oldy = y
    oldfield = field[y][x]

and this in checkadj(x,y):
    
    if noadj and (y!=oldy or x!=oldx):
        field[y][x] = 0
        y=oldy
        x=oldx

    elif noadj:
        return False
```
### Started to try recursion
I have four modules, one for each direction. The [y+1][x] module looks like this:
```py
    if y!=4 and field[y+1][x] == field[y][x]:
        field[y][x] = 0
        y+=1
        checkadj(x,y)
        return True
```



