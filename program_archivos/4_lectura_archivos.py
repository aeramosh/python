# Abre el archivo "./data/hola_mundo.txt" en modo lectura e 
# imprime su contenido en pantalla.
archivo = open("./data/hola_mundo.txt", "r")
contenido = archivo.read()
print (contenido)
archivo.close()