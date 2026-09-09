#1
suma=0
lista=[]
while True:
    num=int(input("ingrese un numero entero a la lista  0 para terminar de agregar "))
    if num == 0:
        break
    else:
        lista.append(num)


for num in lista:
    suma=suma+num

print("la suma de todos los numero es ",suma)

#2

lista=[]
while True:
    num=int(input("ingrese un numero entero  .. presione 0 para terminar "))
    if num == 0:
        break
    lista.append(num)

print("El maximo es ", max(lista))
print("el minimo es " ,min(lista))

#3

lista=[1,2,3,4]
print(lista)
lista.reverse()
print("lista nueva ")
print(lista)

#4

lista=[]
conteopar=0
conteoimpar=0
while True:
    num=int(input("ingrese un numero entero ... 0 para terminar "))
    if num == 0:
        break
    else:
        if num % 2== 0:
            conteopar+=1
            if num % 3 == 0:
                conteoimpar+=1

print("la cantidad de par fueron ,",conteopar)
print("la cantidad de impar fueron ,",conteoimpar)


#5
multiplicacion=0
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)

num=int(input("ingrese un numero entero a multiplicar "))
for i in lista:
    multiplicacion=i*num
    print(f"{num} x {i} = {multiplicacion}")

#6

lista=[]
while True:
    num=int(input("ingrese un numero entero a la lista ... 0 para terminar "))
    if num == 0 :
        break
    else:
        lista.append(num)

actualizada=set(lista)
print("lista final ",actualizada)

#7

lista=[]
conteo=0
suma=0
while True:
    num=int(input("ingrese un numero entero ...  0 para terminar "))
    if num == 0:
        break
    else:
        lista.append(num)
        conteo+=1
        suma=sum(lista)

promedio=suma/conteo
print("el promedio de los numeros ingresados es de ",promedio)

#8

lista=[]
while True:
    num=int(input("ingrese un numero entero ... 0 para terminar "))
    if num == 0:
        break
    lista.append(num)
print("Lista original ")
print(lista)
sinrepetidos=list(set(lista))
print("lista sin los repetidos " ,sinrepetidos)


#9

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True  

lista = []
while True:
    n = int(input("Ingresa un número entero (0 para terminar): "))
    if n == 0:
        break
    if es_primo(n):   # usamos la función
        lista.append(n)

print("Lista con primos:", lista)


#10

lista=[]
while True:
    num=int(input("ingrese un numero entero ... 0 para terminar "))
    if num == 0:
        break
    lista.append(num)

while True:
    indice = int(input("Ingresa un índice para buscar ( -1 para salir ): "))
    if indice == -1:
        break
    if 0 <= indice < len(lista):
        print("Número en índice", indice, ":", lista[indice])
    else:
        print("Índice fuera de rango")

#11

lista=[]
repetido=0
while True:
    num=int(input("Ingrese un numero entero ... 0 para terminarlo "))
    if num == 0:
        break
    else:
        lista.append(num)
for valor in set(lista):
    repeticiones = lista.count(valor)
    if repeticiones > 1:
        print(f"El número {valor} se repite {repeticiones} veces")

#12

lista=[]
lista2=[]
resultado=[]
for i in range (3):
    num=int(input("ingrese un numero entero  max de 3 veces "))
    lista.append(num)
for i in range(3):
    num2=int(input("ingrese un numero entero max de 3 veces "))
    lista2.append(num2)
print(lista)
print(lista2)
for j in range(len(lista)):
    resultado.append(lista[j]+lista2[j])
print(resultado)

#13 
#Las librerias son conjunto de funciones listas para usar; NumPy = librería especial para cálculos numéricos y arrays grandes.
#Ej de Numpy
import numpy as np
lista =np.array([1,2,3])
lista2=np.array([5,6,7])
suma= lista+lista2
print("El resultado es ", suma)




