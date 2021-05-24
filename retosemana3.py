#logica de los descuentos...
#descuento de 0 a 30 -> descuentos progresivos
#en una lista con muchos diccionarios
#45.117 aplicar descuento de 24%
#45.117 * 24% = 655
#45.177 - 655 = 39.8
#aplicar descuento de 20% sobre lo que quedo
#39.8 * 0.2 = 5151
#39.8 - 5151 = 37.0
#[{"sku": 1, "fecha_expiracion": "", "precio": 753.723, "descuento": 5}, 
# {"sku": 2, "fecha_expiracion": "hoy", "precio": 355.885, "descuento": 2}, 
# {"sku": 3, "fecha_expiracion": "hoy", "precio": 309.222, "descuento": 0}, 
# {"sku": 4, "fecha_expiracion": "hoy", "precio": 867.799, "descuento": 0}, 
# {"sku": 5, "fecha_expiracion": "hoy", "precio": 186.459, "descuento": 3}, 
# {"sku": 6, "fecha_expiracion": "hoy", "precio": 574.783, "descuento": 22}]
import json
from unittest import result
products = json.loads(input()) #transformar string a lista
length = len(products)
contador= 0

for i in range (0, length): # buscar indice de cada elemento de lista
    
    productos = products[i]
    
    keys = productos.keys()
    keys = list(keys)

    values = productos.values()
    values = list(values)
    total = False

    if keys[2] == "precio":
        precio = float(values[2])
        descuento = int(values[3])
        descuento = float(descuento/100)
        descuento = precio * descuento
        resultado = precio - descuento 

        if values[1] == "hoy":
            descuento_hoy = 0.2
            fecha_exp = descuento_hoy * resultado
            resultado = resultado - fecha_exp

    contador += resultado
    
contador = round(contador, 2)
print(contador)
