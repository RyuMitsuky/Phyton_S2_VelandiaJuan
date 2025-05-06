#####Factorial numero entero####

####Se define la variable y se pide el numero a factorizar####

n = int(input("Ingrese el numero: "))

####Se crea una condicion para evitar que se intente factorizar por numeros negativos 
if n >= 0:
    factorial = 1

    ###Se crea un bucle####   
    for i in range (1, n+1):
        print(i)
        ###Se añade la multiplicacion acompañado con el bucle####
        factorial = factorial*i

        ####Por ultimo se imprime el resultado####
    print (f"El factorial de {n} es: {factorial}")


###Si no, si no se cumple la condicion, se escribe lo siguiente#####
else: 
    print("No se puede calcular el factorial")

###Creado por VelandiaJuan#####
