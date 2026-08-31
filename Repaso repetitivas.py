#1
for i in range(2,21,+2):
    print(i)

#2
sumatoria=0
while True:
    num=int(input("ingrese un numero entero hasta q sume 100 "))
    sumatoria += num
    if sumatoria>100:
        break

print("la sumatoria total de los numero ingresados es de " ,sumatoria)

#3
lista=["apple", "banana", "avocado"]
print(lista)
for palabra in lista:
    if palabra[0] == "a":
        print(palabra)

#4
multiplicar=1  
num=int(input("ingrese un numero para multiplicarlo "))
for i in range(1,11):

    multiplicar=num*i
    print (f"{num} x {i} = {multiplicar}")

#5
conteovoca=0
texto=(str(input("ingrese una cadena de texto ")))
for letras in texto:
    if letras in "aeiouAEIOU":
        conteovoca+=1
        print(letras)

print("la cantidad de vocales que tiene es de ",conteovoca)

#6

lista=[1,1,2,3,4,5,5,8,9,10,7,7]
print(lista)
listasin=list(set(lista))
print("sin repetidos ...")
print(listasin )

#7
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 :
        print ("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 3 == 5:
        print("BUZZ")
    else:
        print(i)

#8

cadena="hola hola mundo"
frecuencia={}
palabras=cadena.split()
print(lista)
for i in palabras:
    if i in frecuencia:
        frecuencia[i] +=1
    else:
        frecuencia[i]=1
print(frecuencia)

#9
texto="hola mundo"
vocales="aeiouAEIOU"
print(texto)
for letra in texto:
    if letra not in vocales:
        print(letra)

#10
num=int(input("ingrese un numero entero positivo"))
for i in range(2, num +1):
    primo=True
    for b in range(2,i):
        if i % b == 0:
            primo=False
            break
    if primo:
        print (i)



