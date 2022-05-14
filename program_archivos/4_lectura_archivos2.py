# Pide al usuario un nombre de archivo, 
# abrelo en modo lectura e imprime su contenido en pantalla
nombre = input("Dame el nombre de un archivo de texto ")
archivo = open(f"./data/{nombre}", "r")
contenido = archivo.read()
print (contenido)
archivo.close()