# logical_function
El lindo repo del bello reto #6
# Punto 1 - Figuritas bpnitas 
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
Ver documento: [Figuritas_bonitas.py](/Figuritas_bonitas.py)
# Punto2 - Un carrito 
Este punto se tornó mas facil gracias al desarrollo del punto anterior, sigue exactamente la misma lógica, pero en este caso es area y perímetro de el cículo y el rectángulo.
```python
#Punto 2 reto 6
import math 


def area_y_rodeo(r, b , a):
    rellenito: float = (b*a) + (2*math.pi*(r**2))
    rodeo: float = 2*math.pi*r
    print(f"El area de la figura es: {rellenito} ")
    print(f"Elperimetro de la figura es: {rodeo} ")
# Punto 3 - Animalitos
Hallar el total es tan simple como multiplicar la cantidad de animales de cada especie por su equivalencia en kilos de carne y despues sumar.
```python
# Animalitos
def carnita(N, M, K):
    total: float= 6*N + 7*M + K
    print(f"El total de kilos de carne es: {total}")

carnita(((float(input("Ingrese la cantidad de gallinas: "))), (float(input("Ingrese la cantidad de gallos: "))), (float(input("Ingrese la cantidad de pollitos: ")))))
```
# Punto 4
Para esta función solo hace falta restar la suma de la multiplicación de la cantidad de cada uno de los productos a la cantidad de dinero. En este código lo primero que huci fue declarar e inicialiazar las variables y despues definir otra variable con la función, dependiendo la cantidad de dindero sobrante se escribe un mensaje determinado.
```python
#mami_que_era

print("Ingresa la cantidad de cada porducto que te dijo tu mamá que compraras: ")
P = int(input("Panes: "))
M = int(input("Bolsasa de leche: "))
H = int(input("Huevos: "))
B = int(input("Ingresa la cantidad de dinreo que te dió tu mamá: "))
vueltas_o_deuda : float = B-((P*300)+(M*3300)+(H*350))
if vueltas_o_deuda > 0:
    print(f"Estas son las vueltas que te debe dar el vecino: {vueltas_o_deuda}")
elif vueltas_o_deuda == 0:
    print("Te alcanzó exacto, tu mami es muy pila")
else:
    print(f"Le quedas debiendo al veci: {vueltas_o_deuda}")
```
Ver documento:[#mami_que_era.py](/#mami_que_era)

