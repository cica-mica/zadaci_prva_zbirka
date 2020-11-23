"""
Napravite program koji od korisnika trazi unosenje prirodnog broja n. Program treba pronaci i ispisati na zaslon sve savrsene 
brojeve od 1 do unesenog broja n. 
Broj je savrsen ako je jednak zbiru svih svojih djelioca, ne ukljucujuci njega.
"""

n = int(input('Unesite prirodni broj n: '))
suma = 0

for i in range(1,n):
    for brojac in range(1,i):
        if i % brojac == 0:
           suma += brojac
        else:
           suma = suma
           
    if suma == i:
       print(i,' je savrsen broj.')
    else:
       pass
    suma = 0