"""
Napravite program koji omogucava unos brojeva sve dok se ne unese broj djeljiv sa 3. Program treba na zaslon ispisati 
aritmeticku sredinu unesenih brojeva (ukljucujuci i poslednji uneseni broj)
"""

uneseni_broj = int(input('Unesite cijeli broj: '))


def dok_ne_unese_broj_djeljiv_sa_3(a):

    i = 0
    S = 0
    AR = 0

    while True:
      if a%3 == 0:
          S = S + a
          i+=1
          AR = S/i
          print(AR)
          break
      else:
          S +=a
          i+=1
          a = int(input('Unesite sledeci cijeli broj: ')) 


print(dok_ne_unese_broj_djeljiv_sa_3(uneseni_broj))
