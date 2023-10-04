#Interes compuesto 
def Valorprestamo():
    C = float(input("Ingrese el valor del prestamo: "))
    I = float(input("Ingrese el valor del interés: "))
    N = float(input("Ingrese el  tiempo: "))
    VALOR_PRESTAMO = C * ((1+I)**N)
    print(f"El vealor del prestamo es:{VALOR_PRESTAMO} ")

Valorprestamo()

    