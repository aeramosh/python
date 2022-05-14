#Programa que recibe un conjunto de nùmeros e imprime el más grande. 
#el programa deberá leer los números hasta que el usuario escriba "fin"
#la respuesta de ejecuciòn serà los números fin y el mayor
nums = []
n  = 0
while n != "fin" :
    n  = input("Dame un numero ") #si otro programa lee tu programa no se debe poner un letrero, solo solicitar el número
    if n != "fin" :
        nums.append(int(n))
print(max(nums))  
#este problema requiere espacio en memoria ya que utiliza listas
#puede ser resuelto acumulando en la entrada solo el número mayor para después imprimirlo