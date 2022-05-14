#programa para mostrar datos de una matriz y con listas
import os #se requiere esta libreria para borrar pantalla al iniciar el programa
os.system("cls")
alumnos = int(input("Dame el total de alumnos:"))
calis = [None]*alumnos
for n in range(alumnos) : 
    #range El tipo de datos range se puede invocar con uno, dos e incluso tres parámetros
    #range(min, max, step): 
    #cuando es uno solo es el max, desde 0 hasta max - 1, recuerda el último no cuenta
    calis[n] = int(input(f" Calificación alumno {n+1} : ")) 
    #formato f string igual input (" " + str(n+1) + ": ")
    #esta instruccion hace lo mismo que la anterior --> 
    #calis[n] = int(input("Calificación alumno" + str(n+1) + ": ")) 
nl = [numero_lista + 1 for numero_lista in range(alumnos)] 
#esto es similar a nl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] llega hasta donde quieras o donde llegue la variable alumnos
input("presiona ENTER")
print("num",  " ",  "calis")
for n in range(alumnos) :
    print(nl[n], "     ", calis[n]) 
print(calis, "toda la lista")
input("presiona ENTER")
print(nl[0:2], "de la lista de numeros de lista son los dos primeros datos") #un dato en particular
numbers2 = [3,2,2]
print(numbers2, " esta es una nueva lista de datos")
suma_number = sum(numbers2) # encuentra el número mas bajo 
print("numero sumados de la lista-->", suma_number) # Output: 7
print("promedio de mi lista-->", suma_number / len(numbers2)) # Output: 2.3