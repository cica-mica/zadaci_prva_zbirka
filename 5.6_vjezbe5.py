"""
Potpuno parni brojevi su brojevi kod kojih je svaka cifra paran broj. Napravite program koji za uneseni petocifreni cijeli broj
ispisuje je li ili nije potpuno paran.
"""

uneseni_broj = int(input('Unesite zeljeni cijeli petocifreni broj: '))

while True:
    if uneseni_broj >= 10000 and uneseni_broj < 100000:
        break
    else:
        a = int(input('Niste unijeli petocifren broj. Molimo pokusajte ponovo: '))
        print(a)
        uneseni_broj = a

uneseni_broj = str(uneseni_broj)

for i in range(len(uneseni_broj)):
    if int(uneseni_broj[i]) % 2 == 0:
        if i == (len(uneseni_broj)- 1):
            print('Unijeli ste potpuno paran broj.')
        else:
            continue
    else:
        print('Broj koji ste unijeli nije potpuno paran.')
        break
 
