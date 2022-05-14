#programa tipos de datos y prioridad de los operadores
a = int()
a = 2
b = 3
d = "es el resultado"
print("Hola cachondo")
print("Ahora vamos a sumar dos números:", a, "+", b, "=")
c = a + b
print (c, d)
print(type(c))
e = float(input("Dame un numero decimal ")) 
#un imput siempre captura un string, con esto lo convierto a decimal
print("Escribe tu nombre")
nom1 = input()
print("Hola", nom1)
print("¿Cuál es el nombre de tu esposo?")
nom2 = input()
nom5 = input("¿Cuánto quieres a tu esposo? ")
nom3 = nom1 + " y " + nom2
print(nom3)
print(nom1 + nom2)
nom4 = "Amor"
nom4 += " "
nom4 += "por siempre"
print (nom4)
print ("mostrar un entero a cadena " + str(c))
buscar_subcadena = nom4.find("siempre")
#recuerda el valor de la variable es Amor por siempre la subcadena es 9
print(buscar_subcadena)
mensaje = "Hola Adriana" #el espacio antes del igual y después aquí fue importante
extraer_subcadena = mensaje[1:8] #comienza en la posición 0 y se detiene en la 8 sin tomarla en cuenta
print(extraer_subcadena)
print("convertir un string a float y luego a entero")
x = "123.0"
print(x, type(x))
x = float(x)
print(x, type(x))
x = int(x)
print(x, type(x))
c = a * b / (a - b) * a 
print(c)
print(2**2)#elevar a una potencia

