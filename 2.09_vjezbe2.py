"""
Napravite program koji ce pronaci i ispisati broj n za koji vazi da je 1*2*3*...*n = 3628800.
"""
import math

faktorijal_broja = 3628800
n = 2

while faktorijal_broja % n == 0:
    faktorijal_broja = faktorijal_broja/n
    n +=1

print(n-1)