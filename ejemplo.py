# Primitivos 

#my_char = "a" #variable

#print(type (my_char))
# cuando divido / me toma la parte flotante... pero si hago // toma parte entera
#print(5+4)
#print("Mi nombre es", "Python.", end="")
#print(" Monty Python.")
#print("Mi", "nombre", "es", "Monty", "Python.", sep="...")
#print("Mi", "nombre", "es", "Monty", "Python.", sep=" ")
#print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
#print("Mi", "nombre", "es", sep=" ", end=" * ")
#print("Monty", "Python.", sep="*", end="*\n")
#print(0o123) # numero octal 83
#print(0x123) # numero hexadecimal 291
#print(3E8)
#print("Me gusta \"Monty Python\"")
#print('Me gusta "Monty Python"')
#print("Estoy\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\" ")
#print(9 % 6 % 2)

# Caclulo de la hypothenusa
#a = 3.0
#b = 4.0
#c = (a ** 2 + b ** 2) ** 0.5
#print("c =", c)

#operadores cortos
#i=1
#j=1
#i += 2 * j
#print(i)

#convertir millas a kilometros

#kilometros = 12.25
#millas = 7.38

#millas_a_kilometros = 1.61 * millas
#kilometros_a_millas = kilometros/1.61

#print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
#print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

# codifica aquí tus datos de prueba. 3x3 - 2x2 + 3x - 1
#x = -1
#x = float(x)
#x = (3 * (x ** 3)) - (2 * (x ** 2)) + (3*x) - 1
#y = x
#print("y =", y)

#Triangulo rectangulo
#cateto_a = float(input("Ingresa la longitud del primer cateto: "))
#cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
#print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))

#prueba laboratorio
#x = float(input("Ingresa el valor para x: "))
#y = 1 / (x + (1/(x + (1 /(x+(1/x))))))# coloca tu código aquí
#print("y =", y)

# lee tres números
#numero1 = int(input("Ingresa el primer número:"))
#numero2 = int(input("Ingresa el segundo número:"))
#numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

#numeroMayor = max(numero1,numero2,numero3)

# imprimir el resultado
#print("El número más grande es:", numeroMayor) 

#var = input("escribe: ")

#if var == "espatifilo":
#    print("No, ¡quiero un gran Espatifilo!")
#elif var == "Espatifilo":
#    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
#else:
#    print(f"¡Espatifilo! ¡No {var}!")
#ingreso=float(input("Ingrese el ingreso anual:"))

#if ingreso <= 85528:
#    impuesto = (.18 * ingreso) - 556.2
#    impuesto=round(impuesto, 0)
#    if impuesto <=0:
#        print("El impuesto es: 0.0 pesos")
#    else:
#        print("El impuesto es: ", impuesto, "pesos")
#else:
#    impuesto = 14839.2 + (.32*(ingreso-85528))
#    impuesto=round(impuesto, 0)
#    print("El impuesto es: ", impuesto, "pesos")

#año = int(input("Introduzca un año:"))

#if año >= 1582:
#    #año_comun = año%4
#    if (año%4)!= 0:
#        print("Año común")
#    else:
#        print("Año bisiesto")
#else:
#    print("No dentro del período del calendario gregoriano")

# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int (input("Introduce un número o escribe -1 para detener:"))

# Imprimir el número más grande
print("El número más grande es:", numeroMayor)