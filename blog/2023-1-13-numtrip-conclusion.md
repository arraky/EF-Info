# What was it all for?
In my opinion,the goal of this game was to introduce us students to the fundamentals of Python. We knew the game mechanics from the very beginning, we had total freedom on what approach we would take. Everyone took his own approach, some parts in the code will strongly resemble each other, but as long as everybody knows what their code does, who cares?

I'm now able to have an idea, and know how to do it in python, based on my current knowledge. For example, I currently think about trying to program a chess board in python that could take inputs from played games in the common chess notation (e.g. Nxg4). 

# The realisation of the game
## Requirement
+ Python 3.10 (2.0 is outdated and syntax is different)
## Top-Down
[Link to Top-Down-Diagram](/blog/2023-1-23-numtrip-topdown.md)
## Explanation of my refill field function
```py
def replacetop():
    adjlist.sort()
    for i in range(len(adjlist)):
        dy = adjlist[i][0] #easy life expressions
        dx = adjlist[i][1]
        while dy != 0:
            field[dy][dx] = field[dy-1][dx]
            field[dy-1][dx] = 0
            dy-=1 #go up one field
        field[0][dx] = 2**(randint(0,3)) #fill up the field at the top with a new number
```
Adjlist is the list containing the emptied fields. It now sorts the list, the fields at the top will go through the following algorithm first, preventing some errors.

```py
for i in range(len(adjlist)):
```
Repeat the algorithm for every element in the Adjlist

```py
dy = adjlist[i][0]
dx = adjlist[i][1]
```
This makes working and writing the code substantially easier as the name is way shorter. Now to the actual algorithm:
```py
while dy != 0:
    field[dy][dx] = field[dy-1][dx]
    field[dy-1][dx] = 0
    dy-=1 
field[0][dx] = 2**(randint(0,3)) 
```
In short, the algorithm takes the element 'i' in the adjlist and takes the value from the cell above our emptied cell. It repeats this until we hit the top by using a while loop that always goes up one cell.
```py
dy-=1 #this makes the whole loop repeat until we hit the top
```
Once we hit the top, we can't take no number from above anymore, so we generate one instead:
```py
field[0][dx] = 2**(randint(0,3))
```
# Biggest challenge
## Frustration while trying to get the recursion to work
I've never done a recursion code before, but I knew intuitively what it was supposed to do. I tried and tried and in my mind, my codes made sense, but the program didn't *get* them. I felt stupid and annoyed with myself for taking so long getting it to work.

The rest was pretty easy in comparison
# My advice for new students
## Take use of the things you learned
Especially lists, those are very important and make the game development a lot easier and more enjoyable in general.
## Keep at it!
There's nothing like the euphoria you get when something that you've been working on for months suddenly works flawlessly 