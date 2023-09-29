# logical_function
El lindo repo del bello reto #6
## Punto 1 - Figuritas bpnitas 
Para hacer el punto 1 es necesario tener en cuenta los sigientes aspectos:
+ Area y Volumen de una esfera y un cono:
  ![image](https://github.com/mvarelau/logical_function/assets/141885396/13774f92-f734-44ca-a842-8d0619804494)
+ Python tiene un codigo predeterminado en el que define numeros irracionales importantes, funciones algebraicas y más; este código se llama *math*. En este caso de gran utilidad la función que define `pi`:
```python
import math
math.pi
```
Ya para lo siguiente es definir un afuncion que calcule el area y el volument con los argumentos `r1`, `r2` y `h` y correr la función inicializando las variables como *float* e *input*:
```python
#Reto 6 punto 1
import math


def funcion_area_and_volume(r1, r2, h ):
    g: float = ((r2**2) + (h**2))**0.5
    area_superficial = (4 * math.pi * (r1**2)) + (math.pi * r2 + g) #Area de la esfera + area del cono
    volumen = (4/3* math.pi*(r1**3) ) + (1/3 * math.pi * (r1**2)*h)#Volumen esfera + volumen cono 
    print(f"El area superficial de la figura es: {area_superficial}")
    print(f"El volumen de la figura es: {volumen}")


funcion_area_and_volume((float(input("Ingrese el radio de la circunferencia:"))), (float(input("Ingrese el radio del cono: "))),(float(input("Ingrese la altura del cono: "))))
```
Ver documento: 
