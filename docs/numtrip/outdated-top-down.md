# Numtrip Top Down
## Create Playground
### Make Field
Create a pleasing UI with rows, coloumns and a field numbering at the sides

    def fieldnum():
        print('  ',end='')
        for i in range(Row):
            print('    ',i, end=' ')
        print('')
That's the numbering on top of the field (Coloumns)

    def line():
        print('  ', end='')
        for i in range(Row):
            print('+------',end='')
        print('')

That's the dividing line between each row

    def playground():
        fieldnum()
        for i in range(Row):
            line()
            print(i,end=' ') #*
            for j in range(Coloumns):
                if field[i][j] >=10:
                    len = ' '
                else:
                    len = '  '
                print(f'|  ',field[i][j], end=len)
            print('|')
        line()

Integrates the aforehand made definitions 

#* integrates row numbering as well

    playground()

### Generate Numbers
Generate powers of 2 in a field matrix. Starts the game with random numbers

## Playing
### Ask player to choose a field
Ask for Row and Coloumn that the chosen field is in, and save it as "The Chosen one" for now
### Checking for same numbers
Mark all the directly adjacent fields to "The Chosen one" that happen to have the same number
### Marked fields treatment
Remove the numbers in the adjacent fields and multiply the Chosen one by 2.
Empty fields should be replaced with fields from above

