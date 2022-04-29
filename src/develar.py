# develar.py

from PIL import Image
from src.procesa_datos import *

def develar(ruta_imagen, archivo):
    try:
        imagen = Image.open(ruta_imagen, 'r')
    except FileNotFoundError:
        print("Ha ocurido un error al intentar leer los archivos")

    mensaje = ""
    iterador_imagen = iter(imagen.getdata())

    while(True):
        pixeles = valores_pixel(iterador_imagen)

        mensaje_binario = ""

        for i in pixeles[:8]:
            if (i % 2 == 0):
                mensaje_binario += '0'
            else:
                mensaje_binario += '1'

        mensaje += chr(int(mensaje_binario, 2))

        if ("@%#=" in mensaje):
            file = open(archivo, "w")
            file.write(mensaje[:-4])
            file.close()
            return
