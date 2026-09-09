#1
for i in range(1,100+1):
    print(i)
#2

num=int(input("ingrese un numero entero "))
digitos=len(str(num))
print(f" la cantidad de digitos de " ,num , "es de" ,digitos)

#3

num1= int(input("Primer número: "))
num2 = int(input("Segundo número: "))

suma = 0
# calculamos e mostramos en pantalla el resultado
if num1< num2:
    for i in range(num1 + 1, num2):
        suma = suma + i
else:
    for i in range(num2 + 1, num1):
        suma = suma + i
print("La suma es:", suma)


#4
suma=0
while True:
    numero=int(input("ingrese un numero para sumar o cero para terminar "))
    if numero != 0:
        suma=suma+numero
    else:
        break

print("Sacando cuentas ... ")
print(f"la cantidad total de los numeros ingresados es de ",suma)

#5

import random
Conteo=0
num1=random.randint(1,10)
while True:
    num2=int(input("Adivina el numero del 1 al 10 "))
    Conteo +=1
    if num2 == num1:
        print("Felicidades adivinaste")

        break

print(f"Con un total de intentos de ",Conteo)


#6
for i in range(100,0,-2):
    print(i)

#7
num=int(input ("ingrese un numero"))
suma=0
for i in range (1,num+1):
   suma += i 
print("La suma de todos los números desde 0 hasta", num, "es:", suma)

#8
par=0
impar=0
negativos = 0
positivos = 0
for i in range(1,10):
    num=int(input("ingrese un numero"))
    if num % 2 == 0 :
        par+=1
    elif num % 3 == 0 :
        impar+=1
    if num>0:
        positivos+=1
    else:
        negativos+=1

print("la pares fueron  " ,par)
print("los impares fueron ",impar)
print("los positivos fueron ",positivos)
print("los negativos fueron " , negativos)    

#9
suma=0
for i in range (1,10):
    num=int(input("ingrese un numero para calcular la media "))
    suma+=num

media= suma /10
print("la media de los numeros ingresados es de ",media)

#10
num(int("ingrese un numero de dos o mas digitos para revertirlon "))
invertido=0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print("Número invertido:", invertido)


