"""
Dovrsite program koji radite za vase biologe. Koristeci naredbu FOR napravite program kojim cete omoguciti unos temperature
zraka za 7 dana u nedelji. Program treba izracunati i ispisati na zaslon prosjecnu nedeljnu temperaturu.
"""

class Temperature():
    def __init__(self, temperature):
        self.temperature = temperature



monday = Temperature(temperature = int(input('Ponedeljak: ')))
tuesday = Temperature(temperature = int(input('Utorak: ')))
wednesday = Temperature(temperature = int(input('Srijeda: ')))
thursday = Temperature(temperature = int(input('Cetvrtak: ')))
friday = Temperature(temperature = int(input('Petak: ')))
saturday = Temperature(temperature = int(input('Subota: ')))
sunday = Temperature(temperature = int(input('Nedelja: ')))

avredge_temp = (monday.temperature+ tuesday.temperature+ wednesday.temperature+ thursday.temperature + friday.temperature + saturday.temperature + sunday.temperature)/7

print(avredge_temp)
