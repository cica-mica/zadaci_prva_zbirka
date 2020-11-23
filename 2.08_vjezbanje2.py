"""
Napravite program koji ce od korisnika traziti unosenje dva cijela broja. Program treba ispisati rezultat i ostatak 
cjelobrojnog dijeljenja tih brojeva koristeci samo operacije sabiranja i oduzimanja. 
"""

a = int(input('Unesite prvi cijeli broj: '))
b = int(input('Unesite drugi cijeli broj: '))


def poredjenje_dva_broja(a,b):
    m = 1
    kolicnik = 0
    ostatak = 0

    if a>=b:
        while m<= a:
            if abs(a)==m* abs(b):
                kolicnik = m
                ostatak = 0
                print(kolicnik)
                print(ostatak)
                break
            else:
                if abs(a) - m* abs(b) < 0:
                    kolicnik = m-1
                    ostatak = abs(b) + abs(a) - m* abs(b)
                    print(kolicnik)
                    print(ostatak)
                    break
                else:
                    m +=1
    else:
        while m<= b:
            if abs(b)==m* abs(a):
                kolicnik = m
                ostatak = 0
                print(kolicnik)
                print(ostatak)
                break
            else:
                if abs(b) - m* abs(a) < 0:
                    kolicnik = m-1
                    ostatak = abs(a) + abs(b) - m*abs(a)
                    print(kolicnik)
                    print(ostatak)
                    break
                else:
                    m+=1

poredjenje_dva_broja(a,b)


