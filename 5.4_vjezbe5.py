"""
Napravite program koji na zaslon ispisuje sve brojeve izmedju 100 i 200 djeljive sa 26.
"""

a = 100
b = 200

while a < b:
    if a % 26 == 0:
        print(a)
        a += 26
    else:
        a +=1
