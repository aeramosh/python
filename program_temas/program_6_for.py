#ciclo for con listas
nums = [4, 78, 9, 84]
for n in nums:
    print(n)
for i in range(11): #asume que el minimo valor es 0, el maximo 11 y el incremeto 1
    print(i)
print("________________")
for i in range(11, 20):
    print(i)
print("________________")
for z in range(0, 10 , 2):  #el primer valor min, segundo max, tercero incremento 
    print(z)
print("________________")
for y in range(len(nums)): #len devuelve la longitud de la lista, el tamaño de la lista comienza en
    #siempre en 0 y se detiene en el ùltimo valor, es decir, si nums es cuatro el ùltimo que imprime es
    #el valor que esta en la posiciòn 3
    print(nums[y])
print("________________")
nums2 = []
print(len(nums2))
tam = input("Dame de que tamaño quieres crear una lista ")
tam = int(tam)
for a in range(tam):
    nums2.append(a+1)
    print(nums2[a])