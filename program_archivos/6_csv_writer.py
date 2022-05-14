# Crear un archivo csv con el nombre que quieras 
# que tenga una fila especificando que información tendrá cada columna, 
# y una segunda fila con tu información personal. 
# El archivo CSV (Valores Separados por Comas) se debe ver así cuando se abra en una herramienta de hojas de cálculo:
# NOMBRE          APELLIDO PATERNO     APELLIDO MATERNO    EDAD
# Gustavo Dario   Martinez             Ramos               22
import csv
misDatos = [
          ["NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "EDAD"],
          ["Gustavo Dario", "Martinez", "Ramos", "22"]
          ]

with  open("./data/datos.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(misDatos)
     
print("Writing complete")
# con with open el archivo se queda cerrado
