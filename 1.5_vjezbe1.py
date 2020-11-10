"""
Vasa mladja sestra u sestom razredu jako se muci sa razlomcima. Zbog svoje brzine u zadacima cesto ima netacne rezultate. Da joj 
pomognete napravite program kojim ce moci provjeriti resenja dobijena u zadacima. Program treba omoguciti unos brojioca i imenioca
dva razlomka. Nakon toga prikazati izbornik sa sledecim operacijama: sabiranje, oduzimanje, mnozenje i deljenje. U zavisnosti od 
odabira, program na zaslon ispisuje resenje, takodje u obliku razlomka.  
"""

brojilac_1 = int(input('Upisite brojilac prvog razlomka: '))
imenilac_1 = int(input('Upisite imenilac prvog razlomka: '))
brojilac_2 = int(input('Upisite brojilac drugog razlomka: '))
imenilac_2 = int(input('Upisite imenilac drugog razlomka: '))

brojilac = brojilac_1*imenilac_2 + brojilac_2*imenilac_1
imenilac = imenilac_1*imenilac_2

if brojilac%imenilac == 0:
    brojilac = brojilac//imenilac
    imenilac = 1
elif imenilac%brojilac == 0:
    imenilac = imenilac//brojilac
    brojilac = 1
else:
    for brojac in range(max(brojilac, imenilac)):
        if brojilac%(brojac+1) == 0 and imenilac% (brojac+1) ==0:
            brojilac = brojilac// (brojac+1)
            imenilac = imenilac//(brojac+1)
            print(brojilac)
            print(imenilac)
        

print('Brojilac je ', brojilac)
print('Imenilac je ', imenilac)