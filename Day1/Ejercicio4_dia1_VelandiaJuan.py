########Sabers si un numero es primo#####

n = int (input("Ingresa un numero: "))

x = 1
c = 0

while x <= n: 
    if n % x == 0: 
        c = c + 1

    x = x + 1
if c == 2:
    print("El numero ",n, "es primo ")
else:
    print("No es primo el numero ",n,)

