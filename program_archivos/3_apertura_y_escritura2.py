# Pide al usuario el nombre de un archivo de texto y abrelo en modo escritura. 
# Después, pide al usuario lo que quiere que se escriba en este archivo. 
# En este ejercicio, se recopilarán y escribirán en el archivo las líneas que 
# el usuario ingrese, hasta que este escriba "FIN
informacion = "vacio"
nombre = input("Dame el nombre de un archivo de texto ")
archivo = open(f"./data/{nombre}", "w")
print("Escribe lo que quieres que guarde tu archivo o FIN para terminar ")
while informacion != "FIN" :
    informacion = input("--> ")
    if informacion == "FIN" : break
    archivo.write(f"{informacion}\n") 
archivo.close()