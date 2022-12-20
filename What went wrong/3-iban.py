'''
Probe EF 2022
Programm 3-IBAN.py
'''

iban_numbers = [
    'GB33BUKB20201555555555', 
    'CH75512108001245126199', 
    'DE75512108001245126198', 
    'FR7630006000011234567890189',
    'ZZ59ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
]

def copy(list):
    '''
    Gibt eine Kopie der eingegebenen Liste zurück 
    '''
    copied = list
    return copied

def mod97(iban):
    '''
    Berechnet die Checksumme der IBAN. Ist diese gleich 1,
    so ist die IBAN valide, sonst ist irgendwo ein Fehler drin.
    '''
    iban = iban[4:] + iban[:4]
    iban = iban.upper()
    for letter in 'ABCDEFGHIJKLMNOPQRSTUFWXYZ':
        nr = 'ABCDEFGHIJKLMNOPQRSTUFWXYZ'.index(letter) +10
        iban = iban.replace(letter, str(nr))
    remainder = int(iban) % 97
    return remainder

def to_checksum(ibans):
    '''
    Gibt eine Liste mit den checksums zurück
    '''
    checks = copy(ibans)
    for i in range(len(checks)):
        checks[i] = mod97(checks[i])
    return checks

def country_code(iban):
    return str(iban)[:2].upper()

def to_country_codes(ibans):
    '''
    Gibt eine Liste mit den Ländercodes zurück
    '''
    country_codes = copy(ibans)
    for i in range(len(country_codes)):
        country_codes[i] = country_code(country_codes[i])
    return country_codes

def show(ibans):
    '''
    Zeigt eine Übersicht der übergebenen IBANS an
    '''
    checksums = to_checksum(ibans)
    countries = to_country_codes(ibans)
    print('IBANS                                 Country Code     IS VALID')
    print('---------------------------------------------------------------')
    for i in range(len(ibans)):
        print(f'{str(ibans[i]).rjust(35, " ")}             {countries[i]}         {checksums[i] == 1}')


show(iban_numbers)