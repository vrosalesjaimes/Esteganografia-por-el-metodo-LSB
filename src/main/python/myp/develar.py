import numpy as np
from PIL import Image

def codificar(direccion_imagen, direccion_mensaje, resultado):

    imagen = Image.open(direccion_imagen, 'r')
    ancho, alto = imagen.size
    imagen_arreglo = np.array(list(img.getdata()))
    direccion_imagen = resultado

    if imagen.mode == 'RGB':
        n = 3
    elif imagen.mode == 'RGBA':
        n = 4
        
    pixeles_totales_imagen = array.size//n

    bits_ocultos = ""

    for i in range(pixeles_totales_imagen):
        for j in range(0,3):
            bits_ocultos += (bin(array[i][j])[2:][-1])

    bits_ocultos = [bits_ocultos[i:i+8] for i in range(0,len(bits_ocultos),8)]

    mensaje = ""
    for i in range(len(bits_ocultos)):
        if mensaje[-6:] == "ne$dWG":
            break
        else:
            mensaje += chr(int(bits_ocultos[i],2))
    if "ne$dWG" in mensaje: 
