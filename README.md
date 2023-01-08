# Esteganografía por el método LSB
La esteganografía es el conjunto de técnicas algorítmicas para ocultar un conjunto de datos en otro de forma que los primeros no sean evidentes, permanezcan íntegros y sean recuperables mientras que los segundos, a los que se les denomina portadores, no deben verse alterados de manera evidente. Un método común es ocultar mensajes de texto claro en archivos de imágenes. Se aprovecha en este caso el hecho de que, con frecuencia, las imágenes no requieren de preservar todos los datos que contienen para ser útiles.

Un método usado para almacenar un archivo de texto en una imagen consiste en usar el bit menos significativo de cada byte de datos de la imagen para guardar un bit de los datos a ocultar. Por supuesto se supone que la cantidad de bytes de datos de la imagen es suficiente para guardar el archivo de texto respectivo. Típicamente cada pixel de una imagen es una terna (o cuarteta si existe un canal alfa para la transparencia) de bytes, uno para especificar el tono del pixel en el canal rojo, otro para el canal verde y un tercero para el canal azul. Si se cambia el valor del bit menos significativo de cada uno de estos canales, el color del pixel será cambiado de manera imperceptible para quien observa a simple vista la imagen, así que por cada pixel hay, el menos, tres bits útiles para almacenar datos ocultos. 
Por supuesto se está suponiendo que, una vez puestos los bits de datos a ocultar en la imagen, estos permanecerán en la imagen de manera íntegra, por lo que no se deberán usar formatos de compresión con pérdida para guardar las imágenes que contienen datos ocultos usando este esquema.

# Descripción
Se debe implementar un programa que oculte o devele un mensaje en una imagen, se pide que la entrada del programa sean las siguientes:

**Ocultar**
 - La opción **h**
 - El nombre del archivo que contiene el mensaje a ocultar
 - El nombre del archivo de imagen
 - El nombre el archivo de imagen resultante con los datos ocultos
 
 **Develar** 
 
 - La opción **u**
 - El nombre del archivo con la imagen que contiene los datos ocultos
 - El nombre del archivo en el que se guardará el texto develado
 
 # Requisitos
 
 - Python 3.8 o superior

# Repositorio
Se puede clonar el repositorio con el siguiente comando:

    git clone https://github.com/vrosalesjaimes/Esteganografia-por-el-metodo-LSB.git

 # Ejecución
 Una vez clonado el repositorio accedemos al directorio **Esteganografia-por-el-metodo-LSB** o desde línea de comando podemos acceder a dicha carpeta con el comando
 

    cd Esteganografia-por-el-metodo-LSB

  Una vez en dicha carpeta podemos ejecutar el programa:
  **Ocultar:**

    python3 main.py -h [mensaje] [imagen_con_extension] [imagen_salida_con_extension]
 
Incluimos algunos ejemplos de prueba (estos mismos pueden ser ejecutados):

    python3 main.py -h ejemplos/ej1.txt ejemplos/1.png salida1.png
    python3 main.py -h ejemplos/ej2.txt ejemplos/2.png salida2.png

**Develar**

    python3 main.py -u [imagen_con_mensaje_con_extensión] [archivo_de_texto_resultante]

Incluimos algunos ejemplos de prueba (estos mismo pueden ser ejecutados):

    python3 main.py -u salida1.png ej1.txt
    python3 main.py -u salida2.png ej2.txt
# Pruebas
Para ejecutar las pruebas unitarias, desde la carpeta raíz, hacemos uso del comando:

    python3 -m unittest -v
# 
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)