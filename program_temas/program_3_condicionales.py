#programa para ver condicionales y operador not
print("Hola vamos a ver si reunes los requisistos para tomar bebidas alcoholicas")
nom = input("Escribe tu nombre ")
edad = int(input("Escribe tu edad "))
vive = input("Escribe ¿vives con tus papas? (si/no) ")
per = input("Escribe ¿tienes permiso de tus papas? (si/no) ")
mayor_edad:bool = edad >= 18 #te retorna un booleno poner dos puntos y bool es opcional
tengo_permiso = per == "si" #si se compara con == y es el mismo valor da verdadero
vive_papas = vive == "si" #el igual es asignación de un valor a una variable
#el doble igual es comparación, en este caso compara el valor de la variable vive
#si el valor es si devuelve un booleano (true o false)
if  mayor_edad and (tengo_permiso or not vive_papas) :
    print(nom, "ya puedes brindar")
else :
    print(nom, "no puedes tomar") 

