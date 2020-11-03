"""
Napravite program kojim cete pomoci svojoj razrednoj u ispisivanju svjedocanstava. Omogucite joj unos datuma u obliku: dd.mm.gggg. 
Upisani datum ispisite na zaslon tako da mjesec umjesto brojem bude ispisan njegovim nazivom.
"""
uneseni_datum = input('Unesite datum: ')
niz_datuma = uneseni_datum.split('. ')

dan = niz_datuma[0]
mjesec = niz_datuma[1]
godina = niz_datuma[2]

datum_rodjenja = ['januar', 'februar', 'mart', 'april', 'maj', 'jun', 'jul', 'avgust', 'septembar', 'oktobar', 'novembar', 'decembar']

mjesec = mjesec.replace(niz_datuma[1], datum_rodjenja[int(mjesec)-1])
uneseni_datum = dan + mjesec + godina
print(dan, '. ', mjesec, godina, '.')