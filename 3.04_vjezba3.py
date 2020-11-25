"""
Napravite program koji ce traziti unosenje koeficijenata kvadratne jednacine. Program treba na zaaslon ispisati resenja zadate
kvadratne jednacine.
"""
import cmath

a = int(input('Unesite koeficijent ispred nepoznate (x)2: '))
b = int(input('Unesite koeficijent ispred nepoznate x: '))
c = int(input('Unesite slobodni koeficijent: '))

def solving_square_equation(a,b,c):

    x1 = (-b - cmath.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b + cmath.sqrt(b**2 - 4*a*c))/2*a


    return x1, x2

print(solving_square_equation(a,b,c))