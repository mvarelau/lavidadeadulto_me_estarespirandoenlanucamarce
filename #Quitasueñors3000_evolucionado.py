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

    


        
    
    
