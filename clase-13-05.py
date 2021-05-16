#goverment program

distance = float(input("A que distancia vive de la escuela: "))
paramet = input("km o metros: ? ")

if paramet == "km" or "kilometro":
    if distance <= 40:
        brothers = int(input("Cuantos hermanos tiene? : "))
        if brothers >= 2:
            money_family = float(input("Ingrese economia de familia: "))
            if money_family <= 1000:
                print("elegible")
        else:
            print("No elegibe")
elif paramet == "m" or "metros":
    distance = distance*1000
    distance = distance/distance
    if distance <= 40:
        brothers = int(input("Cuantos hermanos tiene? : "))
        if brothers >= 2:
            money_family = float(input("Ingrese economia de familia: "))
            if money_family <= 1000:
                print("elegible")
        else:
            print("No elegibe")   
distancia = int(input('ingrese los kilometros de distancia en numeros: '))
Hermanos = int(input('ingrese cantidad de hermanos que tiene: '))
ingresos = int(input('ingrese ingresos familiares: '))

print("ok")if distancia < 40 and Hermanos > 1 and ingresos in range(1,1000) else print("no")
     