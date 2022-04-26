import numpy as np
from PIL import Image

def codificar(direccion_imagen, mensaje, resultado):

    imagen = Image.open(direccion_imagen, 'r')
    ancho, alto = imagen.size
    imagen_arreglo = np.array(list(img.getdata()))
    direccion_imagen = resultado

    if imagen.mode == 'RGB':
        n = 3
    elif imagen.mode == 'RGBA':
        n = 4
        
    pixeles_totales_imagen = array.size//n

    mensaje =+ "ne$dWG"
    mensaje_binario = ''.join([format(ord(i), "08b") for i in message])
    pixeles_minimos_imagen = len(mensaje_binario)

    if pixeles_minimos_imagen > pixeles_totales_imagen :
        print("ERROR: Se necesita un archivo de mayor tamaño")
    else :
        indice = 0 
        for i in range(pixeles_totales_imagen):
            for j in range(0,3):
                if indice < pixeles_minimos_imagen:
                    imagen_arreglo[i][j] = int(bin(imagen_arreglo[i][j])[2:9] + mensaje_binario[indice],2)
                    indice += 1

        imagen_arreglo = imagen_arreglo.reshape(alto, ancho, n)
        imagen_nueva = Image.fromarray(array.astype('uint8'), imagen.mode)
        imagen_nueva.save(resultado)
