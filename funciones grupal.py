#1

def calcular_factura_final(monto_base: float, impuesto: float = 21.0, descuento: 
float = 0.0, envio_prioritario: float | None = None) -> float:  
    precio_descuento= monto_base * (1 - descuento / 100)
    precio_con_impuesto=precio_descuento * (1 + impuesto / 100)
    total=precio_con_impuesto

    if envio_prioritario is not None:
        total= total + envio_prioritario

    return round(total,2)

    

print(calcular_factura_final(1000.0))
print(calcular_factura_final(1000.0, descuento=10.0))
print(calcular_factura_final(1000.0 ,impuesto=10.0,descuento=5.0,envio_prioritario=150.0))

#2


class ValidadorFinanciero:

    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        
        return len(cuit) == 11 and cuit.isdigit()

    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float, comision: float = 0.02) -> float:
  
        monto_convertido = monto * tasa_cambio
        descuento_comision = monto_convertido * comision
        return monto_convertido - descuento_comision



print(ValidadorFinanciero.es_cuit_valido("20384920194")) 
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05)) 

#3


class Notificador:
    def enviar_recibo(self, cliente: str, total: float) -> None:
        """
        Imprime un resumen formal del cobro.
        """
        print(f"=== COMPROBANTE DE PAGO ===")
        print(f"Cliente: {cliente}")
        print(f"Total abonado: ${total:.2f}")
        print(f"===========================")


class ProcesadorPagos:
    def __init__(self, notificador: Notificador = None):
        """
        Inicializa el procesador. Si no se pasa un notificador externo, 
        instancia uno por defecto (Inyección de dependencias).
        """
        self.notificador = notificador if notificador is not None else Notificador()

    def procesar_transaccion(self, cliente: str, items: list[dict], descuento_cupon: float = 0.0) -> float:
        """
        Calcula el total del carrito, aplica el descuento y delega el recibo al notificador.
        """
        # Sumar los precios de todos los productos en el carrito
        subtotal = sum(item["precio"] for item in items)
        
        # Aplicar el descuento del cupón
        total = subtotal - descuento_cupon
        
        # Garantizar que el total no sea negativo si el cupón supera el costo
        if total < 0:
            total = 0.0
            
        # Delegar la emisión del comprobante al objeto notificador
        self.notificador.enviar_recibo(cliente, total)
        
        # Retornar el total cobrado según el requerimiento técnico
        return total

carrito = [{"nombre": "Teclado", "precio": 50.0}, {"nombre": "Mouse", "precio": 30.0}] 
procesador = ProcesadorPagos() 
procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0) 

#4


def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    """
    Genera un reporte multi-línea utilizando concatenación de strings directa.
    """
    # 1. Cabecera con el módulo en mayúsculas y su salto de línea
    reporte = f"--- AUDITORÍA DE SISTEMA: {modulo.upper()} ---\n"
    
    # 2. Procesamiento de mensajes secuenciales
    reporte += "MENSAJES:\n"
    for indice, mensaje in enumerate(mensajes, start=1):
        reporte += f"[{indice}] {mensaje}\n"
        
    # 3. Procesamiento de metadatos clave-valor
    reporte += "METADATOS:\n"
    for clave, valor in metadatos.items():
        reporte += f"{clave.upper()}: {valor}\n"
        
    # Retorna el string acumulado (quitamos el último salto de línea sobrante)
    return reporte.strip()

log = generar_auditoria_sistema(
    "AUTH", 
    "Intento fallido", 
    "Bloqueo de IP", 
    usuario="admin", 
    ip="192.168.1.10"
)

print(log)


#5


class CalculadoraFitness:
    # No requiere __init__ ya que es un contenedor puramente estático.

    @staticmethod
    def calcular_imc(peso_kg: float, altura_m: float) -> float:
        """Calcula el IMC usando la fórmula: peso / (altura^2)."""
        return peso_kg / (altura_m ** 2)

    @staticmethod
    def clasificar_nivel(imc: float) -> str:
        """Clasifica el rango de salud según el IMC provisto."""
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"


class Atleta:
    def __init__(self, nombre: str, peso: float, altura: float):
        """Inicializa la entidad del atleta con sus datos físicos bases."""
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def obtener_reporte(self, incluir_recomendacion: bool = False, **metricas_extra) -> str:

        imc_calculado = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        rango_salud = CalculadoraFitness.clasificar_nivel(imc_calculado)

        
        reporte = f"--- REPORTE DE ATLETA: {self.nombre.upper()} ---\n"
        reporte += f"IMC: {imc_calculado:.2f} ({rango_salud})\n"

        if metricas_extra:
            reporte += "MÉTRICAS ADICIONALES:\n"
            for clave, valor in metricas_extra.items():
                reporte += f"- {clave.replace('_', ' ').capitalize()}: {valor}\n"

        
        if incluir_recomendacion:
            reporte += "RECOMENDACIÓN: "
            if rango_salud == "Bajo peso":
                reporte += "Se sugiere aumentar el plan calórico y de fuerza.\n"
            elif rango_salud == "Normal":
                reporte += "Excelente estado. Mantener el ritmo de entrenamiento actual.\n"
            else:
                reporte += "Se aconseja ajustar la dieta y priorizar ejercicios cardiovasculares.\n"

        
        return reporte.rstrip()

atleta1 = Atleta("Santiago Fabris", peso=70.0, altura=1.70)

reporte_final = atleta1.obtener_reporte(
    incluir_recomendacion=True, 
    grasa_corporal="18%", 
    frecuencia_cardiaca_reposo="62 bpm"
)

print(reporte_final)
