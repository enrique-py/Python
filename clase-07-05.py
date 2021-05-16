import math

#Lista en python
my_list = [True, "String", 1, 3.4, False]
#print(my_list)
my_list[0] = False
#print(my_list)

# tuplas python, no se pueden asignar valores despues
my_tupla = (True, "String", 1, 3.4, False)
#print(my_tupla[2])

# Diccionario
my_dict = {"name":"Juan", "surname":"Morales", "email":"test@test.com"}
#print(my_dict["name"])
my_dict2 = {"name":"Juan", "surname":"Morales", "class_scores":[5, 1, 3, 0, 1]} 
#print(my_dict2["class_scores"])
#print(my_dict2["class_scores"][2])
my_dict2 = {"name":"Juan", "surname":"Morales", "class_scores":[5, 1, 3, 0, 1]} 
#my_dict3 = {"key-1":input("value-1: "), "key-2":input("value-2: ")}
#print(my_dict3)

#funciones
def sum_two_numbers(number_a, number_b):
    result = number_a + number_b
    print(f"The sum of {number_a} and {number_b} is: {result}")

def tangent_of_angle(angle):
    angle=float(angle)
    result = math.tan(angle)
    print(f"The tangent of {angle}  is: {result}")

angulo=tangent_of_angle(input(" write the angle: "))
