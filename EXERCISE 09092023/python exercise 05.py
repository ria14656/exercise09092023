#crear y cargra una lista con 5 enteros por teclado.
#implementar un algoritmo que identifique el menor de la lista y
#la posicion donde se encuentra.
lista=[]
for x in range (5):
    valor=int(input("ingrese valor:"))
    lista.append(valor)

menor=lista[0]
posicion=0
for x in range (1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x

print("lista completa")
print(lista)
print("menor de la lista")
print(menor)
print("posicion del menor en la lista")
print(posicion)
