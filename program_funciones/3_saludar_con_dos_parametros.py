# función sin retorno de valores
# función con dos parámetros, nombre y edad, string y entero
#Escribe una función que reciba como parámetro un nombre y la edad (entero)
#e imprima un mensaje que diga si esa persona puede o no comprar alcohol. 
def saludar(nombre, edad):
  if edad >= 18:
    print("El jóven " + nombre + " tiene " + str(edad) + " Ya puede tomar alcohol, nada con exceso, todo con medida")
    #el anterior ejemplo con f string seria así:
    #print(f"El jóven {nombre} tiene {edad} Ya puede tomar alcohol, nada con exceso, todo con medida")
    print(f"El jóven {nombre} tiene {edad} Ya puede tomar alcohol, nada con exceso, todo con medida")
  
saludar("Diego", 18)  # llamada a la función, enviando dos parámetros
