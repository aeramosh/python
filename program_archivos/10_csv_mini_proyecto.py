# mini proyecto
# ejemplo para imprimir con orden:
# print(a.ljust(15)[0:9]) donde a es la variable string, l de left, 15 son los espacio que deja y 10 caracteres que trunca
# print(num.rjust(3,"0")) donde num es la variable numerica, r de right, y 0 el caracter que rellena antes del valor numerico

import csv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def recolectar_informacion():
    nom = input("Nombre: ")
    paterno = input("Apellido Paterno: ")
    materno = input("Apellido Materno: ")
    califi = float(input("Calificación: "))
    info = [nom, paterno, materno, califi] 
    return info

def obtener_calificacion(alumno): # recibe un registro
    return alumno[3] # retorna la calificacion del registro

def obtener_nombre(alumno):
    return alumno[1], alumno[2], alumno[0]

def imprime_calificacion(lista_parametro, incluye_nl=True): # el paremetro opcional cuando no se pasa toma el valor True
    if incluye_nl:
        encabeza_num = "NUM" + "\t"
        encabeza_num2 = "   " + "\t" 
    else:
        encabeza_num = ""
        encabeza_num2 = ""
    print(encabeza_num + "  NOMBRE"+ "\t" + "APELLIDO" + "\t" + "    APELLIDO" + "\t" + "  CALIFICACION")
    print(encabeza_num2 + "        "+ "\t" + "PATERNO " + "\t" + "    MATERNO " + "\t" + "              ")
    for a in range(len(lista_parametro)):
        print(a+1 if incluye_nl else "", *lista_parametro[a], sep = '          ') 
        # el operador ternario esta expresado en el primer argumento de este print
        # partes del operador ternario:
        # uno: el valor que quieres que tome si True
        # dos: condicional if con un valor o variable booleano
        # tres: else el valor que quieres que tome si False

    return 

registros = []

# lectura de archivo para respaldo en lista
with  open("./data/datosproyecto.csv", newline="") as csvfile:
    lector_archivo = csv.reader(csvfile)
    for linea in lector_archivo:
        linea[3] = float(linea[3])
        registros.append(linea)

while True:
    print(" ")
    print(bcolors.OKBLUE + "INTERFAZ DE COMANDOS:" + bcolors.ENDC)
    print(bcolors.OKGREEN + "[END] [PRINT] [ADD] [UPDATE] [DELETE] [PRINTCALI]" + bcolors.ENDC)
    comando = input(bcolors.OKBLUE + "Escribe un comando en mayúsculas " + bcolors.ENDC)
    if comando == "END" or comando == "end":
        print("---> Hasta la vista baby =)")
        break
    elif comando == "PRINT" or comando == "print":
        imprime_calificacion(registros)
    elif comando == "ADD" or comando == "add":
        informacion_personal = recolectar_informacion()
        registros.append(informacion_personal) 
        print(bcolors.OKCYAN + "registro añadido" + bcolors.ENDC)
        registros.sort(key=obtener_nombre)
    elif comando == "UPDATE" or comando == "update":
        imprime_calificacion(registros)
        num_lista = int(input("Escribe el numero de lista de la calificación a modificar o 0 para cancelar " ))
        if num_lista != 0:
            califi = float(input("Nueva Calificación: "))
            registros[num_lista-1][3] = califi
            print(bcolors.OKCYAN + "calificación modificada" + bcolors.ENDC)
        else :
            comando == "comando incorrecto"
    elif comando == "DELETE" or comando == "delete":
        imprime_calificacion(registros)
        num_lista = int(input("Escribe el numero de lista del alumno a borrar o 0 para cancelar " ))
        if num_lista != 0:
            del registros[num_lista-1]
            print(bcolors.OKCYAN + "registro borrado" + bcolors.ENDC)
        else :
            comando == "comando incorrecto"
    elif comando == "PRINTCALI" or comando == "printcali":
        lista_ordenada = sorted(registros,key=obtener_calificacion,reverse=True)
        imprime_calificacion(lista_ordenada,incluye_nl=False)
    else : 
        print("Utiliza la interfaz de comandos")

with  open("./data/datosproyecto.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(registros) 