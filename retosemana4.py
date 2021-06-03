def clasificacion_huevos(mi_lista):
    huevos_AAA = 0
    huevos_AA = 0
    huevos_A = 0
    huevos_BC = 0
    for huevo in mi_lista:
        if huevo >= 55 and huevo <60:
            huevos_A += 1
        elif huevo >= 60 and huevo <69:
            huevos_AA += 1
        elif huevo >= 69:
            huevos_AAA += 1
        elif huevo < 53:
            huevos_BC += 1
                    
    cajas = calcular_bandejas(huevos_A, huevos_AA, huevos_AAA, huevos_BC)


    # crea el diccionario de resultados con 
    result = [{'tipo_huevo': 'A', 'numero_huevos': huevos_A, 'numero_bandejas': cajas[0]},
               {'tipo_huevo':'AA', 'numero_huevos': huevos_AA, 'numero_bandejas': cajas[1]},
               {'tipo_huevo': 'AAA', 'numero_huevos': huevos_AAA, 'numero_bandejas': cajas[2]},
               {'tipo_huevo': 'BC', 'numeros_huevos': huevos_BC, 'numero_bandejas':cajas[3]}
               ]
    return result
    # prueba

def calcular_bandejas(A, AA, AAA, BC):
    bandeja_A = A//30
    bandeja_AA = AA//24
    bandeja_AAA = AAA//12
    bandeja_BC =  BC//30
    return [bandeja_A, bandeja_AA, bandeja_AAA, bandeja_BC]
	
