# procesa_datos.py

# Convierte en binario de 8 bits
# usando el codigo ascii asociado.
def convierte_en_binario(mensaje):
    lista_binario = []

    for i in mensaje:
        lista_binario.append(format(ord(i), '08b'))

    return lista_binario

def valores_pixel(iterador):
    pixeles = [valor for valor in
                     iterador.__next__()[:3] +
                     iterador.__next__()[:3] +
                     iterador.__next__()[:3]]
    return pixeles

# Modificación de pixeles
def modifica_pixeles(pixeles_imagen, mensaje):
    mensaje_en_binario =  convierte_en_binario(mensaje)
    longitud_mensaje_binario = len(mensaje_en_binario)
    iterador_pixeles = iter(pixeles_imagen)

    for i in range(longitud_mensaje_binario):
        pixeles = valores_pixel(iterador_pixeles)

        for j in range(0,8):
            if(mensaje_en_binario[i][j] == '0' and pixeles[j] % 2 != 0):
                pixeles[j] -= 1

            elif(mensaje_en_binario[i][j] == '1' and pixeles[j] % 2 == 0 ):
                if(pixeles[j] != 0):
                    pixeles[j] -= 1
                else:
                    pixeles[j] += 1

        if(i == longitud_mensaje_binario -1 ):
            if(pixeles[-1] % 2 == 0):
                if(pixeles[-1] != 0):
                    pixeles[-1] -= 1
                else:
                    pixeles[-1] += 1
        else:
            if(pixeles[-1] % 2 != 0):
                pixeles[-1] -= 1

        pixeles = tuple(pixeles)
        yield pixeles[0:3]
        yield pixeles[3:6]
        yield pixeles[6:9]
