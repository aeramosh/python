# Hacer un programa que lea el archivo que se creo que en el ejercicio 2 de la sección anterior. 
# Por cada registro, deberá imprimir:
# "{Nombre completo, empezando por apellidos}, {edad} años de edad."

import csv

with  open("./data/datos2.csv", newline="") as csvfile:
    lector_archivo = csv.reader(csvfile)
    for linea in lector_archivo:
        print(linea[1],linea[2],linea[0],linea[3], "años de edad")
        