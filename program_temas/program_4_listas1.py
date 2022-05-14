#programa para crear listas
import os #se requiere esta libreria para borrar pantalla al iniciar el programa
os.system("cls")
lista = [90, "Python", 3.87]
print(lista[0]) #90
print(lista[1]) #Python
print(lista[2]) #3.87
print(lista, "toda la lista")
print(lista[-1], "ultimo valor") #cuando es negativo muestra el último valor de la lista
lista[1] = 1.57 #asignar un nuevo valor a un elemento de la lista
#si la lista ya tiene un valor se encima el nuevo
print(lista[-2]) #aquí muestra el ultimo y el antepenultimo valor de la lista
print(lista, "toda la lista")
del lista[0] #borro el primer dato de la lista
print(lista, "toda la lista despues de borrar el primer dato")
input("PRESIONA ENTER")
print("LISTAS ANIDADAS")
lista2 = [1, "Hola", 3.67, [1, 2, 3]] #listas anidadas
print(lista2, "toda la lista")
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x, "datos de otra lista, mostrar algunos datos en especifico")
print(x[3][0])    #p
print(x[3][2][0]) #5
print(x[3][2][2]) #7
input("PRESIONA ENTER otra vez1")
l = [1, 2, 3, 4, 5, 6] #sublistas
print(l, "toda la lista para mostrar sublistas")
print(l[0:2]) #[1, 2]
print(l[2:6]) #[3, 4, 5, 6]
print(l[1:], "asume final") #asume que llegara al final de la lista
l2 = [None]*20 #crea 20 espacios vacios en una lista
print(l2)
l3 = [None for i in range(10)] #comprensión de listas
print(l3)
l4 = [numero_lista + 1 for numero_lista in range(10)] #comprensión de listas
print(l4)
input("PRESIONA ENTER otra vez2")
print()
print()
#Métodos listas
l5 = [1, 2]
print("mi lista antes de append-->", l5)
l5.append(3) #añade elemento al final de la lista
print("mi lista después de append-->", l5) #[1, 2, 3]
l6 = [1, 2, 3]
print("mi lista completa es-->", l6) 
l6.reverse()
print("coloca la lista al revés moviendo todos los datos con reverse", l6)
l6.reverse()
print("lista al derecho, la regrese como estaba con otro reverse", l6)
input("PRESIONA ENTER otra vez3")
print()
print()
print("mi lista completa es-->", l6) 
l6.pop(0) #quita un valor de la lista tomando en cuenta su posición
print("mi lista después de pop 0-->", l6, "quitó la posición 0") #[2, 3]
#l6.pop() #cuando lo le especificas posición, quita ultimo valor de la lista 
print("es el valor que quitó al final de la lista ", l6.pop()) #quita el último valor de la lista y lo imprime
#se puede utilizar este valor para asignarlo a una variable o cualquier uso x = print(l6.pop())
print("mi lista como quedó después de pop ()-->", l6, "quito el último valor") #[2]
input("PRESIONA ENTER otra vez4")
print()
print()
l7 = [1, 3]
print("mi lista completa es: ", l7)
l7.insert(1, 2) #añade en la posición 1 el número 2
print("añadió un valor nuevo con insert ", l7) #[1, 2, 3] añade un elemento en una posición o índice determinado
l7.clear()
print("con clear borro toda mi lista", l7) #borra toda los datos de la lista 
input("PRESIONA ENTER otra vez5")
print()
print()
#Operador in, devuelve un booleno (true/false) si encuentra el número en la lista
print(3 in [1, 2, 3])
#Operador not in
print(3 not in [1, 2, 4, 5])
print(3 and 6 not in [1, 2, 4, 5])
#Funciones para listas
print("mi lista completa es: ", l5)
print("len, da el tamaño de mi lista que es: ", len(l5)) #longitud de listas len
numbers = [4, 2, 12, 8]
print("mi lista completa es: ", numbers)
sorted_numbers = sorted(numbers) #crea una copia ordenada sorted que es una función
print(sorted_numbers, "es una copia de la lista, ordenada con sorted") # Output: [2, 4, 8, 12]
reversed_numbers =  list(reversed(numbers)) #crea una copia de la lista con los datos al revés
#no confundir reversed con reverse  l6.reverse() ya que el segundo solo la invierte
#estudiar método que es cuando utilizas un punto que es direrente a una funcion
#ordenado u ordenar es diferente sorted y sort
print(reversed_numbers, "es una copia de la lista, con los datos invetidos con reversed")
input("PRESIONA ENTER otra vez6")
print()
print()
numbers2 = [9, 34, 11, -4, 27]
print("mi lista completa es: ", numbers2)
max_number = max(numbers2) # encuentra el número mas alto 
print("numero mayor-->", max_number) # Output: 34
min_number = min(numbers2) # encuentra el número mas bajo 
print("numero menor-->", min_number) # Output: -4
suma_number = sum(numbers2) # suma los números de una lista
print("numero sumados de la lista-->", suma_number) # Output: 77
print("promedio de mi lista-->", suma_number / len(numbers2)) # Output: 15.4
input("PRESIONA ENTER otra vez7")
print()
print()
palabras = [5, 6, 7, "mi"]
print("mi lista completa es: ", palabras)
palabras.extend("chocolate") #añade un conjunto de elementos al final de la lista
print("mi lista despues de añadir elementos es: ", palabras)
palabras.extend([7, 7, 7])
print("mi lista despues de añadir otros 3 elementos es: ", palabras)