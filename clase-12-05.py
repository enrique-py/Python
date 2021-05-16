#month_number = int(input("Insert a month number:"))

#months = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril",
#        5:"mayo", 6:"Junio", 7:"Julio", 8:"Agosto",
#        9:"Septiembre", 10:"Octubre", 11:"Noviembre",
#        12:"Diciembre"}

#keys = months.keys()
#keys = list(keys)
#values = months.values()
#values = list(values)

#if month_number < 1 or month_number > 12:
#    print("Not valid number")
#else:
#    #month = months[month_number]
#    #print(month)
#    if month_number == keys[0]:
#        print(values[0])
#    if month_number == keys[1]:
#        print(values[1])
#    elif month_number == keys[2]:
#        print(values[2])
#    elif month_number == keys[3]:
#        print(values[3])
#    elif month_number == keys[4]:
#        print(values[4])

año = int(input("Introduzca un año: "))

if año >= 1582:
    if (año%4) != 0 and (año%100) != 0 and (año%400 != 0):
        print("Año común")
    else:
        print("Año bisiesto")
else:
    print("No dentro del período del calendario gregoriano")