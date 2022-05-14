# función con retorno
# Escribe una función llamada suma, que reciba dos números y retorne la suma de ambos

def escribe_suma(a, b):
    suma = a + b   
    return suma
a = int(input("Dame un numero "))
b = int(input("Dame otro numero "))
suma = escribe_suma(a, b)
print(f"La suma de {a} y {b} es: {suma}")