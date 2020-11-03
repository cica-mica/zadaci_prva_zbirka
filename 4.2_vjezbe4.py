
def je_prost(broj):
    """
    Da li je uneseni broj prost?
    boolean
    """
    d = 2
    # d je djelilac, u ovom slucaju najmanji broj veci od 1 koji uzrokuje da uneseni broj bude slozen

    while d<broj:
        # dok je djelilac manji od unesenog broja, petlja se izvrsava
        if broj%d==0:
            return False
             # ako je ostatak 0, broj je slozen, sto znaci da je netacno
        else:
            d=d+1
            # u suprotnom se djelilac povecava za 1 i vraca se na pocetak petlje
    return True
    # uslov je tacan samo kada djelilac od 2 do broja-1 ne dijeli taj broj, pa se vrijednost true vraca tek kada se ispuni while petlja

print(je_prost(int(input('Unesite neki broj '))))
