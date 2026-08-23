# 1

print("HOLA MUNDO") #imprime en pantalla el mensaje 
# 2

print("hola")
name=input ("ingresa tu nombre") #Pide nombre al usuario
print (f"hola {name}") # Muestra en pantalla el saludo al usuario

#3

nombre = input("ingresa tu nombre") # PEDIMOS DATOS AL USUARIO
apellido = input ("ingresa tu apellido")
edad = input("ingresa tu edad")
lugar = input("ingrese de donde es")
print (f"soy {nombre} {apellido}, tengo {edad} años, y vivo en {lugar}.") # RESULTADO FINAL EN PANTALLA

#4

# Pedir al usuario el radio del círculo
radio = float(input("Introduce el radio del círculo: "))

# Calcular el área
area = 3.1416 * radio * radio

# Calcular el perímetro
perimetro = 2 * 3.1416 * radio

# Mostrar el área y el perímetro
print(f"Área del círculo:, {area}")
print(f"Perímetro del círculo:, {perimetro}")

#5

# PEDIMOS DATOS AL USUARIO
segundos = int(input("Introduce la cantidad de segundos: "))
horas = segundos // 3600
# MOSTRAMOS EN PANTALLA EL RESULTADO
print(f"{segundos} equivale a {horas} horas")

#6

# Pedir un número al usuario
numero = int(input("Introduce un número: "))
# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)

#7

# Pedir dos números enteros distintos de cero
numero1 = int(input("Introduce el primer número (distinto de 0): "))
numero2 = int(input("Introduce el segundo número (distinto de 0): "))
# Realizar y mostrar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#8

altura = float ( input("ingrese su altura en metros"))
peso = float   (input ("ingrese su peso en kilogramos"))
msc = peso/ (altura **2 )
print(f"la masa muscular es , {msc}")

#9


# Pedir al usuario la temperatura en grados Celsius
gradocelsius = float(input("Introduce la temperatura en grados Celsius: "))
# Calcular la temperatura en Fahrenheit
gradofahrenheit = (gradocelsius * 9/5) + 32
# Mostrar el resultado
print(f"{gradocelsius} grados Celsius son equivalentes a {gradofahrenheit} grados Fahrenheit.")


#10

# Pedimos los datos correspondientes al usuario
numero1 = float (input ("ingrese el primero numero") )
numero2 = float (input ("ingrese el segundo numero") )
numero3 = float (input ("ingrese el tercer numero") )
# Calculamos el promedio
promedio = float ( numero1 + numero2 + numero3 )/ 3
# Mostramos resultado 
print(f"el promedio de los numero es {promedio}")
