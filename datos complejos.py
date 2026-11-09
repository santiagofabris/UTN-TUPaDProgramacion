#1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas.update({"naranja": 1200 ,"manzana": 1500, "pera": 2300})

print(precios_frutas)

#2

precios_frutas.update({"Banana": 1330 ,"manzana": 1700, "Melón": 2800})

print(precios_frutas)

#3
frutas_sin_precio=[]

#4
contactos={ }
for i in range (5):
    contacto=input("Ingrese el nombre del contacto ")
    if not contacto.isalpha():
        print("Error solo se permite nombre reales ")
        continue
    numero=(input("ingrese el numero de contacto "))
    if not numero.isdigit():
        print("Error solo se permiten numeros " )
        continue
    contactos[contacto]=int(numero)

print (contactos) 

#5
frase=input("ingrese una frase ")
if not frase.replace(" ","").isalpha():
    print("Error solo se permite palabras para la frase")
else:
    palabras=frase.lower().split()
    palabra_solas=set(palabras)
    conteo={}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra]+=1
        else:
            conteo[palabra]=1
    print(f"las palabras unicas son: {palabra_solas}")
    print(f"el recuento es de {conteo}")

#6
promedio = 0
alumnos = {}

for i in range(3):
    nombres_alumnos = input(f"ingrese el nombre de el alumno {i+1} ")

    notas1 = int(input("ingrese la nota 1 del alumno: "))
    notas2 = int(input("ingrese la nota 2 del alumno: "))
    notas3 = int(input("ingrese la nota 3 del alumno: "))

    
    alumnos[nombres_alumnos] = (notas1, notas2, notas3)

for nombres_alumnos, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    
    print(f"El alumno {nombres_alumnos} tiene un promedio de: {promedio}")

#7
parcial1 = set()
parcial2 = set()
while True:
    nota1=int(input("ingrese las notas .. 0 para terminar "))
    if nota1 <0 or nota1>10:
        print("ingresse la nota correspondiente e valida")
        continue
    if nota1 == 0:
        break
    else:
        parcial1.add(nota1)

while True:
    nota2=int(input("ingrese las notas .. 0 para terminar "))
    if nota2 <0 or nota2>10:
        print("ingresse la nota correspondiente e valida")
        continue
    if nota2 == 0:
        break
    else:
        parcial2.add(nota2)


ambos = parcial1 & parcial2
print("Aprobaron ambos:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)


total = parcial1 | parcial2
print("Aprobaron al menos uno:", total)

#8

frutas={
    "manzana":20,
    "banana": 12,
    "naranja": 8,
    "pera": 14
}
while True:
    print("------------MENU FRUTAS-----------------")
    print("1 - VER STOCK DEL MOMENTO")
    print("2 - AGREGAR PRODUCTO AL STOCK")
    print("3 - ELIMINAR PRODUCTO DEL STOCK")
    print("4 - SALIR")
    seleccion=int(input("ingrese las opciones a utilicar (1 AL 4 )"))
    if seleccion < 1 or seleccion > 4:
        print("seleccion incorrecta selecciona otra vez ")
        continue
    else:
        if seleccion == 1:
            print(frutas)
        if seleccion == 2:
            agregado=input("escriba que fruta o producto desea agregar ")
            if agregado in frutas:
                frutas[agregado] += 1
            else:
                frutas[agregado] = 1
            continue
        if seleccion == 3:
            eliminar=input("escribe que elemento desea sacar del stock ").lower()
            
            if eliminar in frutas:
                frutas.pop(eliminar)
            else:
                print("Este producto no esta en stock nuestro")
            continue
        if seleccion == 4:
            print("-------------SALIENDO ------------")
            break            

#9

agenda_semanal= {
    ("22:00", "lunes"): "trabajo",
    ("22:00", "martes"): "trabajo",
    ("22:00", "miercoles"): "trabajo",
    ("22:00", "jueves"): "trabajo",

}
while True:
    print("----MENU AGENDA----")
    print("1 - VER LA AGENDA COMPLETA")
    print("2 - SELECCIONAR UN DIA Y VER QUE HAY")
    print("3 - SALIR DEL MENU")
    
    opcion_agenda=int(input("ingrese las opciones a usar "))
    if opcion_agenda < 1 or opcion_agenda >3:
        print("opcion incorrecta")
        continue
    else:
        if opcion_agenda == 1:
            print (agenda_semanal)
            continue
        if opcion_agenda == 2:
            dia=str(input("ingrese el dia para ver que hay en la agende "))
            hora=str(input("ingrese hora a verificar "))
            if (hora, dia) in agenda_semanal:
                evento = agenda_semanal[(hora, dia)]
                print(f"El {dia} a las {hora} usted tiene: {evento}")
            else:
                print("no hay eventos a esa hora o dia ")
        if opcion_agenda == 3:
            print("-----SALIENDO-----")
            break


#10

paises={
    ("Buenos Aires"):"Argentina",
    ("Paz"):"Bolivia",
    ("Asuncion"):"Paraguay",
    ("Brasilia"):"Brasil"
    }
print(paises)
invertido={}
for pais,capital in paises.items():
    invertido[capital] = pais
print("------INVIRTIENDO--------")
print (invertido)




    
