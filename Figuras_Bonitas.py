#Reto 6 punto 1
import math


def funcion_area_and_volume(r1, r2, h ):
    g: float = ((r2**2) + (h**2))**0.5
    area_superficial = (4 * math.pi * (r1**2)) + (math.pi * r2 + g) #Area de la esfera + area del cono
    volumen = (4/3* math.pi*(r1**3) ) + (1/3 * math.pi * (r1**2)*h)#Volumen esfera + volumen cono 
    print(f"El area superficial de la figura es: {area_superficial}")
    print(f"El volumen de la figura es: {volumen}")


funcion_area_and_volume((float(input("Ingrese el radio de la circunferencia:"))), (float(input("Ingrese el radio del cono: "))),(float(input("Ingrese la altura del cono: "))))
