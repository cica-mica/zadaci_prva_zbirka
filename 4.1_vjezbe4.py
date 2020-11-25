"""
Napravite program koji ce korisniku omoguciti unosenje prirodnog broja n. Program treba izracunati i ispisati na zaslon koliko nula
ima faktorijal unesenog broja.
"""
import math

uneseni_broj = int(input('Unesite prirodan broj n: '))

def check_if_the_number_is_natural(a):
    while True:
        if a > 0:
            return a
        else:
            a = int(input('Ponovo unesite prirodan broj n: '))

check_if_the_number_is_natural(uneseni_broj)
faktorijal = math.factorial(uneseni_broj)
faktorijal = str(faktorijal)
counter = 0

for i in range(len(faktorijal)):
    if faktorijal[i] == '0':
        counter +=1
    else:
        continue

print(counter)
