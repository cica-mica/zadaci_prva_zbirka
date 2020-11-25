"""
Napravite program koji na zaslon ispisuje sve dvocifrene parne brojeve.
"""

initial_value = 10
final_value = 100

while initial_value < final_value:
    if initial_value % 2 == 0:
        print(initial_value)
        initial_value += 2
    else:
        initial_value +=1
