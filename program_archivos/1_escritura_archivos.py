# Abre el archivo de texto "./data/hola_mundo.txt" en modo escritura. 
# Escribe dentro del archivo "Hola mundo". 
# No olvide cerrar el archivo al terminar.
archivo = open("./data/hola_mundo.txt", "w")

archivo.write('Hola mundo')
archivo.close()