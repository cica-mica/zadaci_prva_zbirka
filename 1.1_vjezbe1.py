
"""
Napravite program koji ce ispisati je li srednja cifra unesenog trocifrenog broja parna, neparna ili nula.
"""
x = int(input('Unesite zeljeni broj '))

srednja_cifra = (x//10)%10
print (srednja_cifra)

if srednja_cifra == 0:
    print('Srednja cifra je 0')
elif srednja_cifra % 2 == 0:
    print('Srednja cifra je parna')
else:
    print('Srednja cifra je neparna')