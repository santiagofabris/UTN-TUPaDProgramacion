#Actividades tp condicinal
#1
# pedimos los datos al usuatio
edad = int(input ("ingrese su edad"))
# verificamos q sea mayor o menor y mostramos resultado
if  edad >= 18 :
    print (" es mayor de edad")
else:
    print ("es menor de edad")

#2
# pedimos datos al usuario
nota=int (input("ingrese su calificacion"))
 # calculamos y averiguamos su nota y mostramos resultado
if nota > 10 :
    print("nota invalida")
else:
    if nota >= 6:

        print ("aprobado")
    else:
         print ("desaprobado")
     
#3
# pedimos datos al usuario
numero = int(input("Ingrese un número: "))
# calculamos si es o no par y mostramos resultado
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4
# pedimos datos al usuario
edad = int(input("Ingrese su edad: "))
# calculamos e verificamos q tipo de edad contiene
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5 
# Pedimos datos al usuario
contraseña = input("Contraseña: ")
# Verificamos e controlamos la cantidad de caracteres ingresada
if len(contraseña) < 8:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
elif len(contraseña) > 14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contraseña correcta")

#6 
#Hacemos q el programa imprima 100 numeros aleatorios
import random
import statistics
#Calculamos e verificamos las media , mediana y moda
num=[random.randint(1, 100) for i in range (50)]
media=statistics.mean (num)
mediana=statistics.median(num)
moda=statistics.mode(num)
print (media ,"media")
print (mediana , "mediana")
print (moda , "moda")
if media > mediana:
   print ("segno positivo")
elif mediana > media:
   print ("segno negativo")
else:
   print ("no hay segno")

#7
#Pedimo datos al usuario
palabra = input("Ingrese una frase: ")
#averiguamos sobre la ultima letra y mostramos en pantalla
ultima_letra = palabra[-1]

if ultima_letra in "aeiouAEIOU":
    print("¡")
else:
    print(palabra)

#8
# Pedimos datos al usuario
name=str(input("ingrese su nombre"))
print ("1:MAYUSCULAS")
print ("2:minisculas")
print ("3:Primera letre mayuscula")
opcion=int (input ("selecciona una opcion"))
# Damos opciones a eleccion y mostramos resultado
match opcion:
    case 1:
        print("Resultado:", name.upper())
    case 2:
        print("Resultado:", name.lower())
    case 3:
        print("Resultado:", name.title())
    case _:
        print("Opción no válida. Debes elegir 1, 2 o 3.")

#9
# Pedimos datos al usuario del sismmo
mag = float(input("Ingresa la magnitud del sismo: "))
 #Calculamos y verificamos q tipo de sismo fue
if mag < 3:
    print("Muy leve")

elif mag < 4:
    print("Leve")

elif mag< 5:
    print("Moderado")

elif mag < 6:
    print("Fuerte")

elif mag < 7:
    print("Muy Fuerte")

else:
    print("Extremo")
#10
hemisferio = input("¿En qué hemisferio estás? (N/S): ")
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día: "))
# Primero determinamos la estación en el hemisferio norte
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"

elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"

elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"

else:
    estacion_norte = "Otoño"
# Ahora invertimos si es hemisferio sur
if hemisferio.upper() == "N":
    print("Estás en", estacion_norte)

else:
    if estacion_norte == "Invierno":
        print("Estás en Verano")
    elif estacion_norte == "Primavera":
        print("Estás en Otoño")
    elif estacion_norte == "Verano":
        print("Estás en Invierno")
    else:
        print("Estás en Primavera")