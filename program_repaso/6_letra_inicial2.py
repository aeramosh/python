#Escribe un programa que lea un número N, y lea N nombres de alumnos. 
#Después, el programa recibirá una letra del abecedario
#y deberá imprimir todos los nombres que comiencen con esta letra.
alumnos = []
ban = False
total_alum = int(input("Dame el total de alumnos del grupo "))
for a in range(total_alum):
    alumnos.append(input("Escribe el nombre del alumno " + str(a+1) + " ")) 
letra = input("Dame una letra ") 
for nombre_alumno in alumnos :
    inicial = nombre_alumno[0] 
    if letra == inicial :
        print(nombre_alumno)
        ban = True #el booleano debe comenzar con mayúscula
if not ban :
    print("Fulanito")