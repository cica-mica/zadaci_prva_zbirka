"""
Napraviti matricu u koju korisnike moze da unosi elemente.
"""

A = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0],[0,0,0,0]]

broj_vrsta = len(A)
broj_kolona = len(A[0])

print(broj_vrsta)
print(broj_kolona)
i = 0
j = 0

while i < broj_kolona:
    while j < broj_vrsta:
        print(A[i][j] == input('Unesite element koji odgovara i-toj vrsti i j-toj koloni: '))
        j+= 1
    j = 0
    i += 1

