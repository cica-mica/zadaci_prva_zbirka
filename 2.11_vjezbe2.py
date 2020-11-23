"""
Napravite program koji omogucava unosenje cijelih brojeva sve dok se ne unese 0. Program treba na zaslon ispisati koliko od unesenih 
brojeva ima tacno jednu neparnu cifru.
"""

def niz_cifara_zadatog_broja():

    uneseni_broj = int(input('Unesite cijeli broj: '))
    neparne_cifre = 0
    trazeni_broj = 0

    while uneseni_broj != 0:

       x = str(uneseni_broj)
       y = len(x)
   

       for i in range(y):
           if int(x[i])%2 != 0:
              neparne_cifre +=1 
           else:
              neparne_cifre = neparne_cifre
       print(neparne_cifre)
       if neparne_cifre == 1:
           trazeni_broj+=1
       else:
           trazeni_broj = trazeni_broj
       print(trazeni_broj)
       neparne_cifre = 0

       uneseni_broj = int(input('Unesite sledeci cijeli broj: '))
    print(trazeni_broj)

   

niz_cifara_zadatog_broja()