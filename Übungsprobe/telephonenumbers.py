telephonebook = '''
+41 044 861 80 94 
0041 032 711 76 53 
0914718911 
0041 022 981 26 48 
+41 032 553 74 60 
062 917 48 63 
052  917  51  46
+1 208-699-0411'''

swissnumbers = []
numbers = telephonebook.split('\n')[1:]
for number in numbers:
    number = number.replace(' ','')
    if '+1' in number:
        number = ''
    elif '+' in number:
        number = number[3:]
    elif '00' in number:
        number = number[4:]
    
    number = number[:3] + ' ' + number[3:6] + ' ' + number[6:8] + ' ' + number[8:10]
    
    swissnumbers.append(number)
    while '   ' in swissnumbers:
        swissnumbers.remove('   ')

print(swissnumbers)



    


