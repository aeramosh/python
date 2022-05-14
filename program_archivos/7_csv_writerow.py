# Crear un programa que pregunte al usuario por la cantidad de personas que se desean registrar. 
# Después, recolectar la información para cada persona y 
# Añadir un registro por cada uno en un nuevo archivo, con el nombre que quieras.
# Recomiendo utilizar el conocimiento que ya tienen sobre funciones para crear una 
# función recolectar_informacion() la cual se encargue de preguntar por la información 
# de una sola persona y devuelva una lista.
import csv

def recolectar_informacion():
    nom = input("Nombre: ")
    paterno = input("Apellido Paterno: ")
    materno = input("Apellido Materno: ")
    edad = int(input("Edad: "))
    info = [nom, paterno, materno, edad] 
    return info

cantidad_personas = int(input("Dame cantidad de personas que se desean registrar: "))

with  open("./data/datos2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "EDAD"])
    for a in range(cantidad_personas):
        informacion_personal = recolectar_informacion()
        writer.writerow(informacion_personal)
