
class celda():
    def __init__(self, fila, columna, valor):
        
        self.fila = int(fila)
        self.columna = int(columna)
        self.valor = str(valor)

class matriz():
    def __init__(self):
        self.celdamatriz = []

    
    def existe_celda(self, fila, columna):
        for celda in self.celdamatriz: 
            if celda.fila == fila and celda.columna == columna:
                if celda.fila == fila or celda.columna == columna:
                    return True
                return True 
        return False


    def obtenerValor(self, fila, columna):
        for celda in self.celdamatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

mi_matriz = matriz()

while True:
    valor = input("ingrese el valor que desea para relllanar la casilla... FIN para terminar ").strip()
    if valor.upper() == "FIN":
        break
    else:
        fila = input("ingrese en que fila rellenamos maximo 10 ")
        if not fila.isdigit():
            print("Solo se permiten digitos")
            continue 
        
        fila = int(fila)
        if fila <= 0 or fila > 10:
            print("Error debe ser entre 1 a 10")
            continue
        else:
            columna = (input("ingrese en que columna ingresa el valor maximo 10 "))
            if not columna.isdigit():
                print("Solo se permiten digitos")
                continue 
            
            columna = int(columna)
            if columna <= 0 or columna > 10: 
                print("Error de parametro debe ser entre 1 al 10")
                continue

            if mi_matriz.existe_celda(fila, columna):
                print("Error casilleros ocupados intente de veulta")
                continue
            else:
                nueva_celda = celda(fila, columna, valor)
                mi_matriz.celdamatriz.append(nueva_celda)
                print("Agregado exitosos")

for celda in mi_matriz.celdamatriz:
    print(f"fila : {celda.fila} , columna {celda.columna} , valor: {celda.valor}")
