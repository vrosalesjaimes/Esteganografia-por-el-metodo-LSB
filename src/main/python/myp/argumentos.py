def bandera_h(arreglo_entrada):
    if "-h" in arreglo_entrada:
        return True
    else:
        return False

def bandera_u(arreglo_entrada):
    if "-u" in arreglo_entrada:
        return True
    else:
        return False

def nombre_archivo_texto(arreglo_entrada):
    if len(arreglo_entrada) == 5 and bandera_h(arreglo_entrada):
        return arreglo_entrada[2]
    else:
        return ""

def nombre_imagen_para_ocultar(arreglo_entrada):
    if len(arreglo_entrada) == 5 and bandera_h(arreglo_entrada):
        return arreglo_entrada[3]
    else:
        return ""

def nombre_imagen_resultante(arreglo_entrada):
    if len(arreglo_entrada) == 5 and bandera_h(arreglo_entrada):
        return arreglo_entrada[4]
    else:
        return ""

def nombre_imagen_para_develar(arreglo_entrada):
    if len(arreglo_entrada) == 4 and bandera_u(arreglo_entrada):
        return arreglo_entrada[1]
    else:
        return ""

def nombre_texto_resultante(arreglo_entrada):
    if len(arreglo_entrada) == 4 and bandera_u(arreglo_entrada):
        return arreglo_entrada[2]
    else:
        return ""
