"""
Stampa najveceg trocifrenog broja na osnovu unesenih cifara
"""

n = int(input('Unesite broj: '))

"""
if n> 100 and n<999:
    return n
else:
    print(int(input('Unesite novi broj: ')))
    return int(input('Unesite novi broj: '))

    if prva> druga and prva>treca:

"""


if n>= 100 and n<= 999:

    a = n//100
    b = (n//10)%10
    c = n%10


    niz_cifara = [a,b,c]
    print(niz_cifara)
    niz_cifara.sort()
    print(niz_cifara)
    niz_cifara = niz_cifara[::-1]
    print(niz_cifara)
    n = str(niz_cifara[0]) + str(niz_cifara[1]) + str(niz_cifara[2])
    print(n)
else:
    uneseni_broj = int(input('Unesite sledeci broj: '))


    