n = int(input('Unesite prirodan broj n ')) 

suma = 0
brojac = 1


while brojac <= n:
    suma = suma + brojac
    print(suma)
    brojac = brojac + 1
    print(brojac)

print(suma)