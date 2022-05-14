#programa para ver elseif
print("Hola vamos a ver si reunes los requisistos para mayor de edad")
nom = input("Escribe tu nombre ")
edad = int(input("Escribe tu edad "))
if edad < 18 :
    print(nom, "Eres menor de edad")
elif edad < 21 :
    print(nom, "Eres mayor de edad en México y menor en USA")
else :
    print(nom, "Eres mayor de edad en México y en USA")

