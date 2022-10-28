def read(Frage):
    inp = input(Frage)
    num=int(inp)
    while num < 1:
            inp = input(Frage)
            num=int(inp)
    return num

def end(inp, sign='*'):
    for i in range(inp):
        print(sign, end='')
    print('')

def mid(inp, sign='*', numh = 1):
    for i in range(numh):
        print(sign,end='')
        for i in range(inp-2):
            print(' ', end='')
        print(sign)

num = read("Gib die Menge an Zeichen pro Zeile ein:")
hei = read("Gib die Menge an Zeilen an:")
sign = input("Art Zeichen:")

numh = int(hei)

end(num, sign)
mid(num, sign, numh-2)
end(num, sign)