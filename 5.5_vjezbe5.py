"""
Napravite program koji na zaslon ispisuje sve trocifrene brojeve cija je prva cifra jednaka poslednjoj.
"""

a = 100
b = 1000

while a < b:
    a = str(a)

    if a[0] == a[len(a) - 1]:
        a = int(a)
        print(a)
        a +=1
    else:
        a = int(a)
        a += 1
