#Programaque recibe un conjunto de números e imprime el tercero más grande.
#el programa deberá leer los nùmeros hasta que el usuario escriba "fin"
#la respuesta de ejecuciòn será el tercero más grande
nums = []
n  = 0
while n != "fin" :
    n  = input( ) #si otro programa lee tu programa no se debe poner un letrero, solo solicitar el número
    if n != "fin" :
        nums.append(int(n))
for i in range(2):
    nums.pop(nums.index(max(nums)))
print(max(nums))
#recuerda, existe la funcion sort, que ordena la lista y con len-3 puedes imprimir el valor que se solicita
