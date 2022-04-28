# develar.py

import numpy as np
from PIL import Image
import os

def develar(direccion_imagen, direccion_mensaje):

    imagen = Image.open(direccion_imagen)
    ancho, alto = imagen.size
    imagen_arreglo = np.array(list(imagen.getdata()))
    archivo = open(direccion_mensaje, 'a')

    if imagen.mode == 'RGB':
        n = 3
    elif imagen.mode == 'RGBA':
        n = 4

    pixeles_totales_imagen = imagen_arreglo.size//n

    bits_ocultos = ""

    for i in range(pixeles_totales_imagen):
        for j in range(0,3):
            bits_ocultos += (bin(imagen_arreglo[i][j])[2:][-1])

    bits_ocultos = [bits_ocultos[i:i+8] for i in range(0,len(bits_ocultos),8)]

    mensaje = ""
    for i in range(len(bits_ocultos)):
        if mensaje[-6:] == "ne$dWG":
            break
        else:
            mensaje += chr(int(bits_ocultos[i],2))
    if "ne$dWG" in mensaje:
        archivo.write(mensaje[:-6])
    else:
        print("No se ha encontrado ningun mensaje")
