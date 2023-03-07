"""
Escribe un programa en Python llamado listaent.py que pida dos números enteros n1 y n2 al usuario
y muestre por consola una lista de n2 números consecutivos a partir de n1. Los números serán
enteros positivos. Si n2 es cero no se generará ninguna lista. El programa controlará los casos
negativos que no cumplan los criterios establecidos.
"""


def generate_List(n1, n2):
    if n2 == 0:
        print("No se generará ninguna lista")
    elif n2 < 0 or n1 < 0:
        print("Los números deben ser enteros positivos.")
    else:
        lista = list(range(n1, n1 + n2))
        print(lista)


n1 = int(input("Introduce el primer número entero: "))
n2 = int(input("Introduce el segundo número entero: "))

generate_List(n1, n2)
