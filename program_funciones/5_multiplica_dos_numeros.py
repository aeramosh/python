# función con retorno
# Escriba una función llamada multiplicación que no utilice el símbolo *,
# sino que utilice la función suma para conseguir el resultado.

def multiplica_con_suma(a, b):
    resultado = 0
    for i in range(a) :
        resultado =  resultado + b
    return resultado
a = int(input("Dame un numero "))
b = int(input("Dame otro numero "))
resultado = multiplica_con_suma(a, b)
print(f"La multiplicacion de {a} y {b} es: {resultado}")