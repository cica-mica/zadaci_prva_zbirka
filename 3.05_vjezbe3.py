"""
Napravite program koji ce od korisnika traziti unosenje dva cijela broja. Nakon toga, na zaslon treba ispisati izbor sledeceg oblika:
Zelite li izracunati:
1. zbir
2. razliku
3. proizvod
4. kolicnik
unesenih brojeva? Upisite broj za izbor:
Nakon sto korisnik upise svoj izbor, potrebno je izracunati rezultat yeljene operacije i ispisati ga na zaslon.
"""

uneseni_broj1 = int(input('Unesite prvi cijeli broj: '))
uneseni_broj2 = int(input('Unesite drugi cijeli broj: '))

print('Zelite li izracunati:')
print('1. zbir')
print('2. razliku')
print('3. proizvod')
print('4. kolicnik')
print('unesenih brojeva?')
izbor = int(input('Unesite broj za izbor: '))

if izbor == 1:
    print(uneseni_broj1 + uneseni_broj2)
elif izbor ==2:
    print(uneseni_broj1 - uneseni_broj2)
elif izbor == 3:
    print(uneseni_broj1 * uneseni_broj2)
elif izbor == 4:
    print(uneseni_broj1//uneseni_broj2)
else:
    print('Kriva operacija!')

