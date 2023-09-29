#Punto 2 reto 6
import math 


def area_y_rodeo(r, b , a):
    rellenito: float = (b*a) + (2*math.pi*(r**2))
    rodeo: float = 2*math.pi*r
    print(f"El area de la figura es: {rellenito} ")
    print(f"Elperimetro de la figura es: {rodeo} ")

area_y_rodeo((float(input("Ingrese el radio de las circunferencias: "))), (float(input("Ingrese la base del rectángulo: "))), (float(input("Ingrese la altura del rectpangulo: "))))