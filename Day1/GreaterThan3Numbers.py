####Encontrar el mayor de 3 numeros python#####


####Se definen las variables
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))
x = int(input("Ingresa un numero: "))


####Se agrega una condicion por si son numeros iguales
if a != b and a != x and b != x:


####Se hace otra condicion pero esta vez agregando comparativas entre > o <
    if a > b:
        if a > x:
            print("El numero mayor es: ", a)
        else:
            print("El numero mayor es:", x)
    else: 
        if b > x: 
            print("El numero mayor es: ", b)
        else:
            print("El numero mayor es ", x)

###por ultimo se imprime el resultado incluyendo si son numeros diferentes####
else: 
    print("ingresa valores diferentes")

####Por ultimo se puede añadir un cronometro para que poder visualizar el resultado####
import time
time.sleep(2)
#####Creado por VelandiaJuan#####




