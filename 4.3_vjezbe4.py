"""
Napravite program koji ce uneseni prirodni broj rastaviti na proste faktore.
"""

uneseni_broj = int(input('Unesite prirodan broj: '))
niz_prostih_djelilaca = []

def check_if_the_number_is_natural(a):
    while True:
        if a > 0:
            return a
        else:
            a = int(input('Ponovo unesite prirodan broj n: '))

i = 1

def broj_je_prost(a):
    d = 2
    while d < a:
        if a % d == 0:
            return False
        else:
            d +=1
    return True

while i < uneseni_broj:
    if broj_je_prost(i) == True:
       if uneseni_broj % i == 0:
           niz_prostih_djelilaca.append(i)
           i +=1        
       else:
           i +=1
           continue
    else:
        i+= 1

print(niz_prostih_djelilaca)
