"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[175],{7386:e=>{e.exports=JSON.parse('{"blogPosts":[{"id":"/2022/12/31/numtrip-update","metadata":{"permalink":"/EF-Info/2022/12/31/numtrip-update","editUrl":"https://github.com/arraky/EF-Info/tree/main/blog/2022-12-31-numtrip-update.md","source":"@site/blog/2022-12-31-numtrip-update.md","title":"Working game?","description":"Inputchecks","date":"2022-12-31T00:00:00.000Z","formattedDate":"31. Dezember 2022","tags":[],"readingTime":4.23,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"nextItem":{"title":"Recursion","permalink":"/EF-Info/2022/12/6/numtrip-update"}},"content":"## Inputchecks\\nI removed the is_integer function and replaced it with a function in the X and Y Inputcheck:\\n\\n    inpx = \\"\\".join(filter(lambda x: x in [\'0\',\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'-\'],input(Questionx))) \\n\\nLambda defines a function here: Filter out everything that\'s not in \'0123456789-\'\\n\\nIt then goes on about and checks if the input is in string \'01234\' and if the len(inpx) is 1. \\nIf that\'s not the case, it tells you to f*ck off.\\n\\njk \\n\\nIt just tells you the input was invalid and the whole process starts anew.\\n\\n## Chechadj()\\nIt has a global adjacent list \\"adjlist\\". TBH I took this idea from Thomas (props to him). \\n\\n- The function now has 4 parameters instead of 2: x,y,oldx and oldy. Again, too fix \\"referenced before assignment errors\\"\\n\\n- Instead of not_left, not_right etc. the functions now check if there is something instead of nothing -> \\n\\n        left = (x > 0 and field[y][x] == field[y][x - 1] and field[y][x]!=0) or False\\n\\n- Now, most importantly, I got the recursion to work: E.g. If left, it appends this field to the adjlist, sets the current field to 0 and repeats the function on the square to the left\\n\\n        if left:\\n            adjlist.append([y,x-1])\\n            field[y][x] = 0\\n            checkadj(x-1,y,oldy,oldx)\\n\\n## Replacetop()\\n- It takes the adjlist and sorts it at the beginning, so that it works from the top of the field downwards. This fixes some errors.\\n- I gave each element in the adjlist a name in a for loop:\\n\\n        for i in range(len(adjlist)):\\n        dy = adjlist[i][0]\\n        dx = adjlist[i][1]\\n- The function takes the number from the field from above and puts it into field[dy][dx] and replaces this top field with 0. Dy is subtracted by 1 and the process begins again for the field that currently has a 0 in it. The moment it reaches the top, it gives this square a new number:\\n\\n        while dy != 0:\\n            field[dy][dx] = field[dy-1][dx]\\n            field[dy-1][dx] = 0\\n            dy-=1\\n        field[0][dx] = 2**(randint(0,3))\\n\\n## Giveup()\\nI provisorically created this function as a jump in for the lack of a working endgame() function. I may change it to a stop game function that saves the current playfield via JSON to another file. \\n\\n## Endgameloss()\\nThis function checks on the whole field, if there\'s even a possible merge of fields. For this, I chose my function chechadj(x,y,oldx,oldy). To make it work, I had to create a new list \\"endgameplayfield\\", which copies the whole content of the playfield\\n\\n    global field\\n    endgameplayfield = [x[:] for x in field]\\n\\nNow in two for loops, it checks if Checkadj() is true. In checkadj() fields change their values though, so in the end, it copies those values back from the endgameplayfield\\n\\n    for i in range(5):\\n        for j in range(5):\\n            if checkadj(j,i, oldx=j, oldy=i) is True:\\n                field = [x[:] for x in endgameplayfield]\\n                adjlist.clear()\\n                return False #Continue game\\nThe return False tells my gameloop to continue. If there\'s no field to merge, you lost and it stops the loop and gives the player a game over message:\\n\\n    print(f\'Alas, you lost! You lasted {roundcount} rounds\')\\n    return True #Loss\\n\\nThe roundcount is in the gameloop\\n\\n## Endgamewin()\\nThis function takes every value in the field and looks for the winning number, I set it to 256 for now. \\n\\n    for i in range(5):\\n        for j in range(5):\\n            if field[i][j] == 256:\\n                return True#Win\\n\\n## Gameloop:\\n\\n    while endgameloss() is False:\\n    if roundcount == 0: #show it the first time\\n        playground()\\n    else:\\n        pass\\n\\n    x = X_Inputcheck(\'X Axis:\') #Inputs\\n    y = Y_Inputcheck(\'Y Axis:\')\\n\\n    oldy,oldx = y,x #Stores values for later\\n    oldfield = field[y][x]\\n\\n    print(f\'You chose the field with the number:\', field[y][x]) #Inform the player that the right field was chosen\\n\\n    checkdel_and_double() #Recursion delete\\n    replacetop() #Fill up\\n\\n    adjlist.clear() #Clear list, so it doesn\'t annoy us in the next round\\n    if endgamewin() is True: #Check if win condition is met; if so -> Congratulations\\n        print(f\'You won! It took you {roundcount} rounds\')\\n        break\\n    roundcount+=1 #counts the rounds\\n    print(\'New Field:\')\\n    playground() #show the end result so that you can play again\\n\\nI wrote the most important infos in it already. \\n\\n1.   It starts by showing the player the playground in round 0. \\n2. Asks for inputs and stores those values for later.\\n3. I added a small print that shows the player the number in the field he chose.\\n4. Goes through the recursion and filling up functions\\n5. Clears the adjlist for the next roudn\\n6. Checks if you\'ve won and shows the amount of rounds it took you\\n7. Adds 1 to the roundcount and shows the new field\\n\\n## Game with variable field sizes\\nIt\'s basically the same thing, I just replaced the hard written code (values like 4 and 5) with variables \\"Col\\" and \\"Row\\". At the beginning of the game, the player is asked for the size of the field. The input is checked through the same functions as X and Y_Inputcheck.\\n\\nI must rewrite it though, as it currently allows for 1x1 fields which obviously don\'t work. And even other fields such as 1x5 tend to have no solution as it\'s all based on random (pseudorandom to be exact) numbers."},{"id":"/2022/12/6/numtrip-update","metadata":{"permalink":"/EF-Info/2022/12/6/numtrip-update","editUrl":"https://github.com/arraky/EF-Info/tree/main/blog/2022-12-6-numtrip-update.md","source":"@site/blog/2022-12-6-numtrip-update.md","title":"Recursion","description":"This is the theme of this blog entry","date":"2022-12-06T00:00:00.000Z","formattedDate":"6. Dezember 2022","tags":[],"readingTime":2.15,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"prevItem":{"title":"Working game?","permalink":"/EF-Info/2022/12/31/numtrip-update"},"nextItem":{"title":"My reentry into Python","permalink":"/EF-Info/2022/08/26/python-reentry"}},"content":"This is the theme of this blog entry\\n\\n## New Functions\\n\\n### Checkdel_and_double()\\nA small function to check if you should double the content of field[y][x]:\\n\\n    def checkdel_and_double():\\n        if checkadj(x,y) is True:\\n            field[y][x] = 2*oldfield\\n            return True\\n\\n### Replacetop()\\nIf the top field is emptied, it can\'t take numbers from above as their are no rows above it (obviously). Thus created a function (haven\'t implemented it yet) that creates new numbers similar to the random numbers filling up field[] at the beginning of the code\\n\\n    def replacetop():\\n        if field[0][x] == 0:\\n            field[0][x] == 2**(randint(0,6))\\n\\n### Endgame()\\nAgain a function that I haven\'t implemented yet. It\'s supposed to constantly check the whole field for a possible field to be marked.\\n\\n    def endgame():\\n        for x in range(4):\\n            for y in range(4):\\n                if field[y][x] != field[y+1][x] or y!=4 and y!=0 or field[y-1][x] and field[y][x+1] or x!=4 and field[y][x-1] or x!=0:\\n                    return True\\n\\n### Is_integer(n):\\nCopied that from the internet. It checks if the input is a float or an integer. Needed it for X- and Y-Inputcheck, because otherwise the program crashed with inputs like \'0.1\'\\n\\n    def is_integer(n):\\n        try:\\n            float(n)\\n        except ValueError:\\n            return False\\n        else:\\n            return float(n).is_integer()\\n\\n## Changes to checkadj(x,y)\\nAdded parameters in paranthesis to account for error \\"referenced before assignment\\"\\n\\n### Added a not_left, not_right etc.\\nstatement with or False at the end so I could all put it into the statement \\"noadj\\"\\n\\n    not_left = (x > 0 and field[y][x] != field[y][x - 1]) or False\\n    not_right = (x < 4 and field[y][x] != field[y][x + 1]) or False\\n    not_up = (y > 0 and field[y][x] != field[y - 1][x]) or False\\n    not_down = (y < 4 and field[y][x] != field[y + 1][x]) or False\\n    noadj = not_left and not_right and not_up and not_down\\n\\n### Added an if and elif statement\\nAfter you check the surroundings of field[y][x], say [y][x+1] and [y][x-1] have the same number in them. My code then empties [y][x] to allow for recursion (otherwise infinite loop between [y][x] and [y][x+1]) and goes to [y][x+1] to check this field\'s surroundings (Recursion). If it doesn\'t find anything new, it should return to the original y and x values to check at [y][x-1]. Thus I added this in my play loop: \\n    \\n    oldx = x\\n    oldy = y\\n    oldfield = field[y][x]\\n\\nand this in checkadj(x,y):\\n    \\n    if noadj and (y!=oldy or x!=oldx):\\n        field[y][x] = 0\\n        y=oldy\\n        x=oldx\\n\\n    elif noadj:\\n        return False\\n\\n### Started to try recursion\\nI have four modules, one for each direction. The [y+1][x] module looks like this:\\n\\n    if y!=4 and field[y+1][x] == field[y][x]:\\n        field[y][x] = 0\\n        y+=1\\n        checkadj(x,y)\\n        return True"},{"id":"/2022/08/26/python-reentry","metadata":{"permalink":"/EF-Info/2022/08/26/python-reentry","editUrl":"https://github.com/arraky/EF-Info/tree/main/blog/2022-08-26-python-reentry.md","source":"@site/blog/2022-08-26-python-reentry.md","title":"My reentry into Python","description":"Introduction","date":"2022-08-26T00:00:00.000Z","formattedDate":"26. August 2022","tags":[],"readingTime":0.66,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"prevItem":{"title":"Recursion","permalink":"/EF-Info/2022/12/6/numtrip-update"}},"content":"## Introduction\\nIn the first second, I was completly lost only understanding the simple commands\\n\\n    from turtle import *\\n\\n    forward(n)\\n    left(m)\\n\\nWhen we had to draw the side of a die that shows a five, my inner perfectionist came out and made a mess of a code:\\n\\n    from turtle import *\\n\\n    forward(2)\\n    left(90)\\n    penup()\\n    forward(2)\\n    dot(10)\\n    right(180)\\n    forward(2)\\n    left(90)\\n    pendown()\\n\\n    forward(76)\\n    left(90)\\n\\n    penup()\\n    forward(2)\\n    dot(10)\\n    right(180)\\n    forward(2)\\n    left(90)\\n    pendown()\\n\\n    forward(2)\\n    left(90)\\n    forward(76)\\n\\n    penup()\\n    left(90)\\n    forward(2)\\n    dot(10)\\n    right(180)\\n    forward(2)\\n    left(90)\\n    pendown()\\n\\n    forward(2)\\n    left(90)\\n    forward(76)\\n\\n    penup()\\n    left(90)\\n    forward(2)\\n    dot(10)\\n    right(180)\\n    forward(2)\\n    left(90)\\n    pendown()\\n\\n    forward(2)\\n    left(90)\\n    forward(38)\\n\\n    penup()\\n    left(90)\\n    forward(40)\\n    dot(10)\\n    right(180)\\n    forward(40)\\n    left(90)\\n    pendown()\\n    forward(36)\\n\\n    hideturtle()\\n\\nThis code........literally repeats itself 3 times. I\'m not quite happy about this code, but I won\'t bother making it any shorter as that\'s where my perfectionism ends :)"}]}')}}]);