#logica de los descuentos...
#descuento de 0 a 30 -> descuentos progresivos
#en una lista con muchos diccionarios
#45.117 aplicar descuento de 24%
#45.117 * 24% = 655
#45.177 - 655 = 39.8
#aplicar descuento de 20% sobre lo que quedo
#39.8 * 0.2 = 5151
#39.8 - 5151 = 37.0

import json

productos = json.loads(input()) #transformar string a lista

#algoritmo
resultado = 5454

print (resultado)

print(productos[0])
