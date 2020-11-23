"""
Napravite program koji ce od korisnika traziti unosenje pozitivnog cijelog broja. Program treba uneseni broj rastaviti na dva 
dijela tako da njihov umnozak bude minimalan
"""

broj_cifara = int(input('Koliko ce vas broj imati cifara? '))
a = 0
niz_cifara = []
broj1 = []
broj2 = []

for i in range(broj_cifara):

    a = int(input('Unesite cifru: '))
    niz_cifara.append(a)

niz_cifara.sort()
print(niz_cifara)