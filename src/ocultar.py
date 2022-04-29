# ocultar.py

from PIL import Image
from src.procesa_datos import *

def ocultar(ruta_imagen, archivo, ruta_imagen_cifrada):
    try:
        imagen = Image.open(ruta_imagen, 'r')
        mensaje = open(archivo).read() + "@%#="
    except FileNotFoundError:
        print("Ha ocurrido un error al intentar leer los archivos")

    a = imagen.size[0]
    (x,y) = (0,0)

    for pixel in modifica_pixeles(imagen.getdata(), mensaje):
        imagen.putpixel((x,y), pixel)
        if(x+1 == a):
            x = 0
            y += 1
        else:
            x += 1

    imagen.save(ruta_imagen_cifrada)
