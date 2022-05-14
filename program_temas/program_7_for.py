#ciclo for, tuplas, captura total alumnos con su nombre y los muestra con su númerados
alumnos = []
total_alum = int(input("Dame el total de alumnos del grupo "))
for a in range(total_alum):
    alumnos.append(input("Escribe el nombre del alumno " + str(a+1) + " ")) 
    #el incremento en uno a+1 solo muestra un numero para el usuario, 
    #no afecta la posición de la lista
for a in range(len(alumnos)):
    print(a+1, alumnos[a])
print("________________")
for a in alumnos:
    print(a)
print("________________")
for tupla in enumerate(alumnos):  
    #enumerate devuelve la posición y el nombre del alumno entre paréntesis, 
    #que son tuplas conjunto de datos fijos
    nl,alumno = tupla
    print(tupla)
    print(nl, alumno)
print("________________")
for nl,alumno in enumerate(alumnos):  #sintaxis llamada descomposición
    #ahora declaro directamente en el for y así me ahorro una variable, visualizo una tupla descompuesta, 
    #la tupla es finita y no es modificable
    print(nl, alumno)