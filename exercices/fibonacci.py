import time
a = [0,1]

def inputcheck(Question):
    rawinp = input('How many fibonacci numbers:')
    while not rawinp.isnumeric():
        print('input not valid')
        rawinp = input('How many fibonacci numbers:')
    n = int(rawinp)
    return n
    
    
def fibonacci():
    n = inputcheck('Fibonacci numbers:')
    t0 = time.time()
    for i in range(n-1):
        a.append(a[i]+a[i+1])
    tx = time.time()
    print(a,tx-t0)

fibonacci()






