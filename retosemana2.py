examen = float(input())
leccion =float(input())
tarea = float(input())
practica = float(input())

resultado = (examen*.45)+(leccion*.25)+(tarea*.15)+(practica*.15)

if resultado >= 4.5:
    print("A")

if resultado <= 4.5 and resultado > 4.0:
    print("B+")

if resultado <= 4.0 and resultado > 3.5:
    print("B")

if resultado <= 3.5 and resultado > 3.0:
    print("C")

if resultado <= 3.0 and resultado > 2.0:
    print("D")

if resultado <= 2.0:
    print("E")