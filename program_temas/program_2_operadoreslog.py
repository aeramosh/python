#programa para ver condicionales y operadores and or
print("Hola vamos a ver si reunes los requisistos para tomar bebidas alcoholicas")
nom = input("Escribe tu nombre ")
edad = int(input("Escribe tu edad "))
vive = input("Escribe ¿vives con tus papas? (si/no) ")
per = input("Escribe ¿tienes permiso de tus papas? (si/no) ")
if edad >= 18 and (per == "si" or vive == "no"):
    print(nom, "ya puedes brindar")
else :
    print(nom, "no puedes tomar") 

