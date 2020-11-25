"""
Napravite program koji ce na zaslon ispisati najmanju cifru unesenog broja.
"""

uneseni_broj = int(input('Unesite zeljeni cijeli broj: '))

uneseni_broj = str(uneseni_broj)

niz_broja = []

for x in range(len(uneseni_broj)):
    niz_broja.append(uneseni_broj[x])

niz_broja.sort()
print(niz_broja[0])