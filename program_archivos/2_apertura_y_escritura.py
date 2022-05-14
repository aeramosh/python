# Pide al usuario el nombre de un archivo de texto y abrelo en modo escritura. 
# Después, pide al usuario lo que quiere que se escriba en este archivo.

nombre = input("Dame el nombre de un archivo de texto ")
archivo = open(f"./data/{nombre}", "w")
informacion = input("Escribe lo que quieres que guarde tu archivo ")
archivo.write(informacion)
archivo.close()