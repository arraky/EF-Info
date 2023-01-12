signcorner='::'
signceiling='='
signwall ='||'
signempty=' '

def askwidth(FrageWidth):
    inp = input(FrageWidth)
    while not inp.isnumeric():
        inp = input(FrageWidth)
    numwidth=int(inp)
    return numwidth

def askheight(FrageHeight):
    inp = input(FrageHeight)
    while not inp.isnumeric():
        inp = input(FrageHeight)
    numheight=int(inp)
    return numheight

def ceiling(numwidth):
    
    print(signcorner, end='')
    for i in range(numwidth):
        print(signceiling, end='')
    print(signcorner)

def wallandroom(numwidth):
    print(signwall, end='')
    for i in range(numwidth):
        print(signempty,end='' )
    print(signwall)

def create():
    
    height = askheight('Height:')
    width = askwidth('Width:')
    ceiling(width)
    for i in range(width):
        wallandroom(width)
    ceiling(width)

create()