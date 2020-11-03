import math

n= int(input('Unesite trocifren broj '))

prva_cifra= n//100
srednja_cifra= (n//10)%10
poslednja_cifra= n%10


def odstampaj_najvecu_cifru(prva, druga, treca):
    if prva > druga and prva > treca:
        return prva
    elif druga > prva and druga > treca:
        return druga
    else:
        return treca

rezultat = odstampaj_najvecu_cifru(prva_cifra, srednja_cifra, poslednja_cifra)
print (rezultat)
rezultat = int(math.sqrt(rezultat))
print(rezultat)