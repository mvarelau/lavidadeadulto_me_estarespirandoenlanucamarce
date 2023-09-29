#mami_que_era

print("Ingresa la cantidad de cada porducto que te dijo tu mamá que compraras: ")
P = int(input("Panes: "))
M = int(input("Bolsasa de leche: "))
H = int(input("Huevos: "))
B = int(input("Ingresa la cantidad de dinreo que te dió tu mamá: "))
vueltas_o_deuda : float = B-((P*300)+(M*3300)+(H*350))
if vueltas_o_deuda > 0:
    print(f"Estas son las vueltas que te debe dar el vecino: {-vueltas_o_deuda}")
elif vueltas_o_deuda == 0:
    print("Te alcanzó exacto, tu mami es muy pila")
else:
    print(f"Le quedas debiendo al veci: {vueltas_o_deuda}")