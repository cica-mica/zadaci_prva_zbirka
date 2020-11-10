"""
Napravite program koji ce za uneseni broj n na zaslon ispisati koliko nula na kraju ima njegov faktorijal.
"""
import math 

n = int(input('Unesite zeljeni broj: '))
n = math.factorial(n)
broj_nula = 0
print(n)

while True:
   if n% 10 == 0:
      broj_nula +=1
      n = n//10
   else:
      break

print(broj_nula) 
