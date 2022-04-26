import sys

def numero_argumentos_validos(arreglo_entrada):
    if len(arreglo_entrada) == 4 | len(arreglo_entrada) == 5:
        return True
    else:
        return False

def bandera_h(arreglo_entrada):
    if "-h" in sys.argv:
        return True
    else:
        return False

def bandera_u(arreglo_entrada):
    if "-u" in sys.argv:
        return True
    else:
        return False


print(numero_argumentos_validos(sys.argv))
print(len(sys.argv))
