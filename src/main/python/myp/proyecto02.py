import sys
from argumentos import *
from ocultar import *
from develar import *

def uso():
    print("Uso: python3 [-h <txt> <img> <img_resultante>] | [-u <img> <txt_resultante>]")
    sys.exit()

entrada = sys.argv
h = bandera_h(entrada)
u = bandera_u(entrada)

if h == u:
    uso()
elif h:
    nombre_txt = nombre_archivo_texto(entrada)
    nombre_img_original = nombre_imagen_para_ocultar(entrada)
    nombre_img_resultante = nombre_imagen_resultante(entrada)
    if nombre_txt == "" or nombre_img_original == "" or nombre_img_resultante == "":
        uso()
    else:
        ocultar(nombre_img_original, nombre_txt, nombre_img_resultante)
        print("Oculta texto en la imagen y la guarda")
elif u:
    nombre_img = nombre_imagen_para_develar(entrada)
    nombre_txt_resultante = nombre_texto_resultante(entrada)
    if nombre_img == "" or nombre_txt_resultante == "":
        uso()
    else:
        develar(nombre_img, nombre_txt_resultante)
        print("Devela texto de la imagen y lo guarda")


