# main.py

import sys
import pathlib
from src.argumentos import *
from src.ocultar import *
from src.develar import *

def uso():
    print("Uso: python3 [-h <txt> <img> <nombre_para_img_resultante>] | [-u <img> <nombre_para_txt_resultante>]")
    sys.exit()

entrada = sys.argv
h = bandera_h(entrada)
u = bandera_u(entrada)

if h == u:
    uso()
elif h:
    nombre_txt = pathlib.Path(__file__).absolute().parent / nombre_archivo_texto(entrada)
    nombre_img_original = pathlib.Path(__file__).absolute().parent / nombre_imagen_para_ocultar(entrada)
    nombre_img_resultante = nombre_imagen_resultante(entrada)
    if nombre_txt == "" or nombre_img_original == "" or nombre_img_resultante == "":
        uso()
    else:
        ocultar(nombre_img_original, nombre_txt, nombre_img_resultante)
elif u:
    nombre_img = pathlib.Path(__file__).absolute().parent / nombre_imagen_para_develar(entrada)
    nombre_txt_resultante = nombre_texto_resultante(entrada)
    if nombre_img == "" or nombre_txt_resultante == "":
        uso()
    else:
        develar(nombre_img, nombre_txt_resultante)
