import math

def area_triangulo(a,b,c):
    s = (a+b+c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print (A)

a, b, c = (input())
a ,b, c = int(a, b, c)
area_triangulo(a, b, c)