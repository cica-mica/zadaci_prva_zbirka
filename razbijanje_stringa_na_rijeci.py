"""
1. Stampati koliko ima rijeci u stringu ako su rijeci odvojene razmacima.
"""

def broj_rijeci(ulazni_string):
    rijeci_niz = ulazni_string.split(' ')
    duzina_niza = len(rijeci_niz)
    return duzina_niza

a = broj_rijeci('Uvod u web programiranje')
print(a)