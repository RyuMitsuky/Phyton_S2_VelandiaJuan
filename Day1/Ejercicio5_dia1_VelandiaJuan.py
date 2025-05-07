####Pasar grados celsius a Fahrenheit#####
####Primero que nada tener en cuenta la formula que es ºF = (ºC ·* 1/8) + 32


####Definimos las variables
def convertir(c):

    ###se aplica la formula 
    return(c * 9/5)+32



###por ultimo se piden los datos y se imprime el resultado##
n = float (input("Ingrese los grados celsius: "))
print (f"la conversion a grados fahrenheit: {convertir(n)}")

##por VelandiaJuan ##
