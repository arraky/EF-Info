'''
Probe EF 2022
Programm 2-EMAIL.PY
'''
#try with telephone numbers different countries and different prefix

verteiler = '''
caesonia.reich@gmail.com;

tulugaq.guidi@gmx.ch;

adisa23.palmisano@hispeed.ch;
chinwendu.maclean96@bluewin.ch;

foteini.faron@outlook.com;
'''

mitglieder = []

# Ziel:
# mitglieder = [                 .
#     ['Caesonia', 'Reich'],     .
#     ['Tulugaq', 'Guidi'],      .
#     ['Adisa', 'Palmisano'],    .
#     ['Chinwendu', 'MacLean'],  .
#     ['Foteini', 'Faron']       .
# ]                              .

mitglieder_raw = verteiler.split('\n')
for i in range(len(mitglieder_raw)):
    try:
        if mitglieder_raw[i] == '':
            mitglieder_raw.pop(i)
    except:
        break


mitglieder_no_at = []
for i in mitglieder_raw:
    try:
        mitglieder_no_at.append(i.split('@')[0])
    except:
        break



for i in mitglieder_no_at:
    mitglieder.append(i.split('.'))


lenmitglieder= len(mitglieder)
mitglieder_big =[]

for i in range(lenmitglieder):
    for j in range(1):
        mitglieder[i] = [j.title() for j in mitglieder[i]]

        full_name = [j.strip('123456789') for j in mitglieder[i]]
        
        mitglieder_big.append(full_name)

for i in range(lenmitglieder):
    for j in range(2):
        print(mitglieder_big[i][j], end=' ')
    print('')

