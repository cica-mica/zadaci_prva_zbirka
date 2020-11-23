"""
Napravite program koji ce na zaslon ispisati aritmeticku sredinu trocifrenih brojeva kojima je poslednja cifra 5 a zbir 
cifara im je 15.
"""

n = 100

a = n//100
b = (n//10)%10
c = n%10

def djeljiv_sa_5_zbir_cifara_15(a,b,c):

    n = 100
   
    i = 0
    S = 0
    AS = 0

    while n<1000:

        a = n//100
        b = (n//10)%10
        c = n%10

        if c==5 and a+b+c == 15:
            S+=n
            i+=1
            n+=1
            AS = S/i
            
        else:
            n+=1
    print(AS)    
    

djeljiv_sa_5_zbir_cifara_15(a,b,c)

