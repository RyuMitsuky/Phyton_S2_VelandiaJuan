#####Factorial numero entero####

####Se define la variable####

n = int(input("Ingrese el numero: "))
if n >= 0:
    factorial = 1
    for i in range (1, n+1):
        print(i)
        factorial = factorial*i
    print (f"El factorial de {n} es: {factorial}")

else: 
    print("No se puede calcular el factorial")


    
