#Genere un programa que reciba un entero n, entre 1 y 20, y que imprima el cubo de
#los números desde 1 hasta n espaciados por un final de línea, avanzando de 1 en 1.

# Ingresa el primer valor
#numero = int(input ("Introduzca un número o escriba -1 para detener:"))

#for numero in range(1, numero+1):
#    numero = numero**2
#    print(numero)

#n = input("inserte el numero:")
#n = int(n)

#acumm = 1

#while acumm <= n:
#    print(acumm ** 3)
#    acumm += 1

#Los palíndromos son frases que se leen igual de derecha de izquierda que de
#izquierda a derecha. Por ejemplo, anita lava la tina es un palíndromo, ya que
#obviando los espacios en blanco, la frase se lee igual. Elabora un programa que diga
#si una frase es un palíndromo o no.

frase = str(input("Ingresa una frase a evaluar: "))
frase = frase.lower()
frase = frase.replace(' ', '')
frase2=len(frase)

while frase2 != "":

    for i in frase:
 
        frase2=len(frase)
        if frase2%2 != 0:
            print(f"la frase “{frase}” es un palíndromo")
            break
        #if frase == frase[::-1]:
        #    print(f"la frase “{frase}” es un palíndromo")
        #    break
        else:
            print(f"la frase “{frase}” No es un palíndromo")
            break

    frase2 = str(input("Ingresa una nueva frase a evaluar o presione enter para salir: "))
    frase = frase2
    
print("gracias")