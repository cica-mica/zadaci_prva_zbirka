"""
Napravite program koji omogucava unosenje cijelih brojeva sve dok se ne unese nula. Program treba na zaslon ispisati koliko od 
unesenih brojeva ima barem jednu parnu cifru.
"""

uneseni_broj = int(input('Unesite cijeli broj: '))
parne_cifre = 0

while uneseni_broj != 0:

   x = str(uneseni_broj)
   y = len(x)
   

   for i in range(y):
      if int(x[i])%2 == 0:
          parne_cifre +=1
      else:
          parne_cifre = parne_cifre
    
   uneseni_broj = int(input('Unesite sledeci cijeli broj: '))

print(x)
print(y)
print(parne_cifre)