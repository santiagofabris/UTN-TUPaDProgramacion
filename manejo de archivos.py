#1
producto_inicio=[
"banana,2000,10 \n",
"manzana,300,5 \n",
"pera,400,4 \n"
]
with open ("productos.txt", "w" ) as archivo:
    archivo.writelines(producto_inicio)
#2
with open ("productos.txt", "r") as archivo:
    for linea in archivo:
            linea=linea.strip()
            if not linea:
                continue
            partes=linea.split(",")
            nombre = partes[0]
            precio = partes[1]
            cantidad = partes[2]
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#3
prod=input("ingrese un producto nuevo ")
precio=int(input("ingrese su precio "))
cantidad=int(input("ingrese la cantidad de producto "))

with open ("productos.txt", "a") as archivo:
    archivo.write(f"{prod},{precio},{cantidad}\n")



#4
productos = []

with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        datos=linea.strip()
        if not datos:
            continue
        datos=datos.split(",")
        productos_nuevos={
            "nombre":datos[0],
            "precio":datos[1],
            "cantidad":datos[2]
        }
        productos.append(productos_nuevos)



nombre_a_buscar=input("ingrese un nombre de producto a buscar en el stock ").strip()
for producto in productos:
    if producto["nombre"].lower() == nombre_a_buscar.lower():
        print ("producto en stock")
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

#6
with open ("productos.txt" , "w") as archivo:

    for producto in producto:
        archivo.write(f"producto{['nombre']},{producto['precio']},{producto['cantidad']}")