from PIL import Image 
import procesa_datos

def develar(ruta_imagen, archivo):
    imagen = Image.open(ruta_imagen, 'r')
    mensaje = ""
    iterador_imagen = iter(imagen.getdata())
    
    while(True):
        pixeles = procesa_datos.trios_pixeles(iterador_imagen)
        
        mensaje_binario = ""
        
        for i in pixeles[:8]:
            if (i % 2 == 0):
                mensaje_binario += '0'
            else:
                mensaje_binario += '1'
        
        mensaje += chr(int(mensaje_binario, 2))
        
        if (pixeles[-1] % 2 != 0):
            file = open(archivo, "w")
            file.write(mensaje)
            file.close()
            return