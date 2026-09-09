#1

def saludar():
    print("hola mundo")
    
saludar()

#2

nombre=input("ingrese su nombre")
def saludar_usuario():
    print ("Holas ", nombre)

saludar_usuario()

#3

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"soy [{nombre}] [{apellido}]  tengo [{edad}] y vivo en [{residencia}]")


nombre=input("ingrese su nombre ")
apellido=input("ingrese su apellido ")
edad=int(input("ingrese su edad "))
residencia=input("ingrese de donde es ")

informacion_personal(nombre, apellido , edad, residencia)

#4

def calular_area_circulo(radio):
    resultado=3.14*radio**2
    print("El resultado del area del circulo es de " , resultado)

def calcula_perimetro_circulo(radio):
    resultadoperimetro=2*3.14*radio
    print("El resultado del perimetro del circulo es de ", resultadoperimetro)


radio=float(input("ingrese el radio a calcular "))


calular_area_circulo(radio)
calcula_perimetro_circulo(radio)

#5
def segundos_a_hora(segundos):
    hora=segundos/3600
    return hora
   

segundos=int(input("ingrese la cantidad de segundos "))
total=segundos_a_hora(segundos)
print(f"la cantidad de {segundos} es a hora un total de {total} hora/s")

#6 

def tabla_multiplicar(numero):
    resultado_tabla=[]
    for i in range(0,11):
        resultado_tabla.append(numero*i) 
    return resultado_tabla

numero=int(input("ingrese un numero para la multiplicacion "))
tabla=tabla_multiplicar(numero)
for i in range (0,11):
    print(f"{numero} x {i} = {tabla[i]}")

#7
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    division=a/b
    multiplicacion=a*b
    return(suma,resta,division,multiplicacion)


a=int(input("ingrese el primer numero "))
b=int(input("ingrese el segundo numero "))

suma,resta,division,multiplicacion=operaciones_basicas(a,b)

print(f"las suma de los numero es {suma}")
print(f"la resta de los numero es {resta}")
print(f"la division de los numero es de {division}")
print(f"la multiplicacion es de {multiplicacion}")

#8

def calcular_imc (peso,altura):
    imc= peso/altura**2
    return imc

peso=float(input("ingrese su peso en KG "))
altura=float(input("ingrese su altura en M2 "))

calculo=calcular_imc(peso,altura)
print("El indice de masa corporal es de ", calculo)

#9
def celsius_fahrenheit(celsius):
    calculo_fahrenheit=(celsius*1.8)+32
    return calculo_fahrenheit

celsius=int(input("ingrese la temperatursa en celsius "))
calculo=celsius_fahrenheit(celsius)
print(f"{celsius} a fahrenheit es {calculo}")

#10

def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    return promedio

a=int(input("ingrese el valor de a "))
b=int(input("ingrese el valor de b "))
c=int(input("ingrese el valor de c "))

calculofinal=calcular_promedio(a,b,c)
print("El promedio de los numeros ingresados es de ",calculofinal)