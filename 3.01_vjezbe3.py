"""
Napravite program koji od korisnika trazi unosenje jednog cijelog broja. Program treba na zaslon ispisati je li uneseni
broj djeljiv sa 3.
"""

uneseni_broj = int(input('Unesite cijeli broj: '))

if uneseni_broj % 3 == 0:
    print('Broj koji ste unijeli je djeljiv sa 3.')
else:
    print('Broj koji ste unijeli nije djeljiv sa 3.')
    