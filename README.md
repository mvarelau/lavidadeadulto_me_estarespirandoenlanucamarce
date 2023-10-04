# logical_function
El lindo repo del bello reto #6
# Punto 1 - Figuritas bonitas 
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
# Punto 3
Para este punto, solo debiamos multiplicar los animales por el peso de su carne y despues sumarlos 
```python
# Animalitos
def carnita(N, M, K):
    total: float= 6*N + 7*M + K
    print(f"El total de kilos de carne es: {total}")

carnita(((float(input("Ingrese la cantidad de gallinas: "))), (float(input("Ingrese la cantidad de gallos: "))), (float(input("Ingrese la cantidad de pollitos: ")))))
````
Ver documento: 
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
# Punto 5 
Para este punto tuve que averiguar cual era la ecuación del interes compuesto:
![image](https://github.com/mvarelau/logical_function/assets/141885396/1b357e7e-df56-4e45-bf7c-204768fe028a)
+ Y despues de eso hice un código en el que el usuario ingresa cada uno de los valores y posteriormente se calcula el prestamo total:
```python
#Interes compuesto 
def Valorprestamo():
    C = float(input("Ingrese el valor del prestamo: "))
    I = float(input("Ingrese el valor del interés: "))
    N = float(input("Ingrese el  tiempo: "))
    VALOR_PRESTAMO = C * ((1+I)**N)
    print(f"El vealor del prestamo es:{VALOR_PRESTAMO} ")

Valorprestamo()
```
Ver documento: 
#Punto 6
El objetivo de este punto fue calcular la cantidad de enfermos en un pais en el que el contagio se duplica diariamente:
```python
#Diosmioseñorsalvanos
def covid():
    D = float(input("Ingrese el numero de días que han pasdo: "))
    C = float(input("Ingrese el número de contagiados hasta hoy: "))
    Numerode_enfermos= (2**D)+C
    print(f"El  número de contgios toltales es:{Numerode_enfermos} ")
covid()
```
Ver documento:
# Punto 7
Quitasueños3000 :)
```python
#Quitasueñors3000_evolucionado
def promedio(a:float, b:float , c:float , d:float , e:float ) -> float:
    Promedio = (a + b + c + d + e)/5
    return Promedio


def mediana(a:float, b:float , c:float , d:float , e:float ) -> float:
#"a" es la mediana
    if c > d > a > b > e or c > d > a > e > b or c > e > a > d > b or c > e > a > b > d or c > b > a > d > e or c > b > a > e > d or d > c > a > b > e or d > c > a > e > b or d > e > a > c > b or d > e > a > b > c or d > b > a > c > e or d > b > a > e > c or e > c > a > b > d or e > c > a > d > b or e > d > a > c > b or e > d > a > b > c or c > d > a > b > e or c > d > a > e > b or c > e > a > d > b or c > e > a > b > d or c > b > a > d > e or c > b > a > e > d or d > c > a > b > e or d > c > a > e > b:
        return a
#"b" es la mediana
    if a > c > b > d > e or a > c > b > e > d or a > d > b > c > e or a > d > b > e > c or a > e > b > c > d or a > e > b > d > c or c > a > b > d > e or c > a > b > e > d or c > d > b > a > e or c > d > b > e > a or c > e > b > a > d or c > e > b > d > a or d > a > b > c > e or d > a > b > e > c or d > c > b > a > e or d > c > b > e > a or d > e > b > a > c or d > e > b > c > a or e > a > b > c > d or e > a > b > d > c or e > c > b > a > d or e > c > b > d > a or e > d > b > a > c or e > d > b > c > a:
        return b 
#"c" es la mediana
    if a > b > c > d > e or a > b > c > e > d or a > d > c > b > e or a > d > c > e > b or a > e > c > b > d or a > e > c > d > b or b > a > c > d > e or b > a > c > e > d or b > d > c > a > e or b > d > c > e > a or b > e > c > a > d or b > e > c > d > a or d > a > c > b > e or d > a > c > e > b or d > b > c > a > e or d > b > c > e > a or d > e > c > a > b or d > e > c > b > a or e > a > c > b > d or e > a > c > d > b or e > b > c > a > d or e > b > c > d > a or e > d > c > a > b or e > d > c > b > a:
        return c
#"d" es la mediana
    if a > b > d > c > e or a > b > d > e > c or a > c > d > b > e or a > c > d > e > b or a > e > d > b > c or a > e > d > c > b or b > a > d > c > e or b > a > d > e > c or b > c > d > a > e or b > c > d > e > a or b > e > d > a > c or b > e > d > c > a or c > a > d > b > e or c > a > d > e > b or c > b > d > a > e or c > b > d > e > a or c > e > d > a > b or c > e > d > b > a or e > a > d > b > c or e > a > d > c > b or e > b > d > a > c or e > b > d > c > a or e > c > d > a > b or e > c > d > b > a:
        return d
#"e" es la mediana
    if b > c > e > a > d or b > c > e > a > d or b > c > e > d > a or b > c > e > d > a or b > d > e > a > c or b > d > e > a > c or b > d > e > c > a or b > d > e > c > a or c > b > e > a > d or c > b > e > a > d or c > b > e > d > a or c > b > e > d > a or c > e > b > a > d or c > e > b > a > d or c > e > b > d > a or c > e > b > d > a or d > b > e > a > c or d > b > e > a > c or d > b > e > c > a or d > b > e > c > a or d > c > e > a > b or d > c > e > a > b or d > c > e > b > a or d > c > e > b > a:
        return e


def promediomultiplicativo(a:float, b:float , c:float , d:float , e:float ) -> float:
    PromedioM = (a* b* c* e* d)/5
    return PromedioM


def ordendescendente(a:float, b:float , c:float , d:float , e:float ) -> float:
     #con a
    if a < b:
        aux=b
        b=a
        a=aux
    if a < c:
        aux=c
        c=a
        a=aux
    if a < d:
        aux=d
        d=a
        a=aux
    if a<e:
        aux=e
        e=a
        a=aux
    #con b
    if b<c:
        aux=c
        c=b
        b=aux
    if b<d:
        aux=d
        d=b
        b=aux
    if b<e:
        aux=e
        e=b
        b=aux
    #con c
    if c<d:
        aux=d
        d=c
        c=aux
    if c<e:
        aux=e
        e=c
        c=aux
    #con d 
    if d<e:
        aux=e
        e=d
        d=aux
    return e, d, c, b, a 


def ordenascendente(a:float, b:float , c:float , d:float , e:float ) -> float:
     #con a
    if a > b:
        aux=b
        b=a
        a=aux
    if a > c:
        aux=c
        c=a
        a=aux
    if a > d:
        aux=d
        d=a
        a=aux
    if a>e:
        aux=e
        e=a
        a=aux
    #con b
    if b>c:
        aux=c
        c=b
        b=aux
    if b>d:
        aux=d
        d=b
        b=aux
    if b>e:
        aux=e
        e=b
        b=aux
    #con c
    if c>d:
        aux=d
        d=c
        c=aux
    if c>e:
        aux=e
        e=c
        c=aux
    #con d 
    if d>e:
        aux=e
        e=d
        d=aux
    return a, b, c, d, e 


def Potencia(a:float, b:float , c:float , d:float , e:float ) -> float:
#mayor
    if a>b and a>c and a>d and a>e:
        mayor=a
    elif b>a and b>c and b>d and b>e:
        mayor=b
    elif c>a and c>b and c>d and c>e:
        mayor=c
    elif d>a and d>b and d>c and d>e:
        mayor=d
    elif e>a and e>b and e>c and e>d:
        mayor=e
#menor
    if a<b and a<c and a<d and a<e:
        menor=a
    elif b<a and b<c and b<d and b<e:
        menor=b
    elif c<a and c<b and c<d and c<e:
        menor=c
    elif d<a and d<b and d<c and d<e:
        menor=d
    elif e<a and e<b and e<c and e<d:
        menor=e
    potencia=mayor**menor
    return potencia


def cubicamenor(a:float, b:float , c:float , d:float , e:float ) -> float:
    if a<b and a<c and a<d and a<e:
        menor=a
    elif b<a and b<c and b<d and b<e:
        menor=b
    elif c<a and c<b and c<d and c<e:
        menor=c
    elif d<a and d<b and d<c and d<e:
        menor=d
    elif e<a and e<b and e<c and e<d:
        menor=e
    cubica = menor**1/3
    return cubica
```
Ver documento:
# Punto 8


    


        
    
    
