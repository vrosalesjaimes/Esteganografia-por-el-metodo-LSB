from PIL import Image 
import procesa_datos

def ocultar(ruta_imagen, archivo, ruta_imagen_cifrada):
    imagen = Image.open(ruta_imagen, 'r')
    mensaje = open(archivo).read()

    img_copia = imagen.copy()
    a = img_copia.size[0]
    (x,y) = (0,0)

    for pixel in procesa_datos.modifica_pixeles(img_copia.getdata(), mensaje):
        img_copia.putpixel((x,y), pixel)
        if(x+1 == a):
            x = 0
            y += 1
        else:
            x += 1

    img_copia.save(ruta_imagen_cifrada)
