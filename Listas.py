lista=list(range(0,100,4))
print (lista)

#2
listas=[]
for i in range(0,5):
    elemento=input("ingrese un elemento").strip()
    listas.append(elemento)

print(listas[3])

#3

vacio=[]
for i in range (0,3):
    cosas=input("ingrese algun elemento")
    vacio.append(cosas)

print("lista actualizada")
print(vacio)

#4

animales=["perro","gato","conejo","pez"]
print(animales)
animales[-1]="loro y oso"
print("lista actualizada")
print(animales)

#5
#Busca al numero maximo de la lista y lo elimina de la lista

#6
lista2=list(range(10,30,5))
print(lista2)

#7

autos=["sedan","polo","suran","gol"]
print(autos)
nuevo=input("ingrese un elemento para la lista")
nuevo2=input("ingrese otro elemento para la lista")
autos[-2]=nuevo
autos[-3]=nuevo2
print("Lista actualizada")
print(autos)

#8

dobles=[]
print(dobles)
numeros=10,20,30
dobles.append(numeros)
print("Lista actualizada")
print(dobles)

#9


compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
print(compras)
agregado="jugo"
compras[2].append(agregado)
print("Actualizamos...")
print(compras)
compras[1][1]="tallarines"
print("Actualizamos ...")
print(compras)
compras[0].remove("pan")
print("Actualizamos ....")
print(compras)

#10
lista_anidada=[15],[True],[25.5,57.9,30.6],[False]
print(lista_anidada[0])
print(lista_anidada[1])
print(lista_anidada[2][0])
print(lista_anidada[2][1])
print(lista_anidada[2][2])
print(lista_anidada[3])


