# Escribe una función que dada una lista, 
# revierta el orden de los elementos en esta.
# NOTA: Hay que revertir los elementos en la lista dada, 
# por lo tanto la función no puede retornar nada.

def revierte_orden(lista_numeros:list):
    for i in range(len(lista_numeros) // 2): #division trunca
        num = lista_numeros[i]
        lista_numeros[i] = lista_numeros[-i - 1]
        lista_numeros[-i - 1] = num
    return 

lista_numeros = [66, 78, 2, 45, 97, 17, 34, 105, 44, 52]
print(lista_numeros)
revierte_orden(lista_numeros)
print(lista_numeros)

