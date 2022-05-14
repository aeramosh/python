#Qué es un iterable
#Un iterable es un objeto que se puede iterar sobre él, es decir, 
#que permite recorrer sus elementos uno a uno. 
#un objeto iterable es aquél que puede pasarse como parámetro de la función iter().
#Esta función devuelve un iterador basado en el objeto iterable que se pasa como parámetro.
nums = [4, 78, 9, 84]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#Un iterador recorre los elementos de un iterable solo hacia delante. 
#Cada vez que se llama a la función next() se recupera el siguiente valor del iterador.