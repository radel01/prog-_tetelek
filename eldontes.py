import math

n = int(input("\nszám: "))
if n < 2:
    prim = False
else:
    i=2
    while i <= math.sqrt(n) and not(n % i == 0):
        i+=1
    prim = i > math.sqrt(n)
print(f"{prim}Prím : Nem prím")
