""""
2. Da li je unesena rijec palindrom?
anavolimilovana
ana
topot
(...)
"""

def da_li_je_palindrom(rijec):
    rijec = rijec.replace(' ','')
    rijec = rijec.lower()
    if rijec == rijec[::-1]:
        return True
    else:
        return False

print(da_li_je_palindrom('Ana voli     Milovana'))
