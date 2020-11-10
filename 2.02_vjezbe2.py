"""
Napravite program koji na zaslon ispisuje kombinaciju cifara a i b za koje vrijedi: (aa)^b = abba
"""

prva_cifra = int(input('Unesite prvu cifru: '))
druga_cifra = int(input('Unesite drugu cifru: '))

lijeva_strana = 10*prva_cifra +prva_cifra
desna_strana = 1000*prva_cifra + 100*druga_cifra +10*druga_cifra + prva_cifra

while True:
    

   if (lijeva_strana)**druga_cifra == desna_strana:
      print(prva_cifra, druga_cifra)
      break
   else:
      prva_cifra = int(input('Uneiste sledecu cifru a: '))
      druga_cifra = int(input('Unesite sledecu cifru b: '))
      lijeva_strana = 10*prva_cifra +prva_cifra
      desna_strana = 1000*prva_cifra + 100*druga_cifra +10*druga_cifra + prva_cifra
      