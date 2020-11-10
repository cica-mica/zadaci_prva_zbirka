"""
Napravite program koji ce na zaslon ispisati koliko ima cetvorocifrenih brojeva ciji je zbir prve i cetvrte cifre jednak umnosku
druge i trece.
"""

n = 1000


def jednakost_zbir_prva_cetvrta_proizvod_druga_treca(a,b,c,d):

    i = 0
    n = 1000

    
    while n< 10000:

        a = n//1000
        b = (n//100)%10
        c = (n%100)//10
        d = n%10

        if a+d == b*c:
            i+=1
            n+=1
        else:
            n+=1
    print(i)
    
a = n//1000
b = (n//100)%10
c = (n%100)//10
d = n%10

jednakost_zbir_prva_cetvrta_proizvod_druga_treca(a,b,c,d)

            