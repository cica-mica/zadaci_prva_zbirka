"""
Napravite program koji ce na zaslon ispisati kvadrat unesenog cijelog broja ako je broj negativan, a u suprotnom njegovu dvostruku
vrijednost.
"""

uneseni_broj = int(input('Unesite zeljeni cijeli broj: '))

def u_zavisnosti_od_prirode_argumenta(a):
    if a < 0:
        return a**2
    else:
        return 2*a

print(u_zavisnosti_od_prirode_argumenta(uneseni_broj))