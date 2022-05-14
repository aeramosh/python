#Escribe un programa que lea un número N, y lea N nombres de alumnos. 
#Después, el programa recibirá una letra del abecedario y deberá imprimir un nombre
#que comience con esta letra.
#En caso de que la letra que se dé no sea la inicial de ninguno de los nombres, imprimir: "Fulanito"
alumnos = []
ban = False
total_alum = int(input("Dame el total de alumnos del grupo "))
for a in range(total_alum):
    alumnos.append(input("Escribe el nombre del alumno " + str(a+1) + " ")) 
letra = input("Dame una letra ") 
for a in range(len(alumnos)) :
    nombre_alumno = alumnos[a]
    inicial = nombre_alumno[0] #es igual a decir inicial = alumnos[a][0] se quitaria linea 10 y 11
    if letra == inicial :
        print(alumnos[a])
        ban = True #el booleano debe comenzar con mayúscula
        break
if ban == False :  #cuando es booleano se puede usar not ban
    print("Fulanito")