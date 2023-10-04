#Diosmioseñorsalvanos
def covid():
    D = float(input("Ingrese el numero de días que han pasado: "))
    C = float(input("Ingrese el número de contagiados hasta hoy: "))
    Numerode_enfermos= (2**D)+C
    print(f"El  número de contgios toltales es:{Numerode_enfermos} ")
covid()