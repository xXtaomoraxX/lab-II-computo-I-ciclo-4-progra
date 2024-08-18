#defininiremos la clase
class DispositivoElectronico:
    #inicializamos la clase con los atributos
    def __init__(self, tipo, modelo, procesador, memoria, almacenamiento, precio_compra):
        #definimos los atributos principales
        self.tipo = tipo
        self.marca = "PHR" #recordar que "PHR" sera la marca de los dispositivos electronicos
        self.modelo = modelo
        self.procesador = procesador
        self.memoria = memoria
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.7#recordar que su precio de venta es igual al precio de compra
        #multiplica por 1.7 para sacar la ganancia de venta
        self.origen = "importado" #recordar que todos los productos seran importados

    def mostrar_informacion(self):
        #usaremos el siguiente metodo para guardar y mostrar la informacion 
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria: {self.memoria} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")
        print(f"Origen: {self.origen}")

# Función para registrar dispositivos
def registrar_dispositivos():
    dispositivos = []

    for _ in range(2):  # Registrar al menos dos dispositivos de cada tipo
        tipo = input("Tipo de dispositivo (celular/tablet/portátil): ")#recordar que la tienda unicamente
        #registra de estos tres tipos de dispositivos
        modelo = input("Modelo del dispositivo: ")
        procesador = input("Procesador del dispositivo: ")
        memoria = int(input("Memoria RAM del dispositivo (GB): "))#la capacidad de memoria RAM tambien sera
        #un valor de tipo entero
        almacenamiento = int(input("Almacenamiento del dispositivo (GB): "))#el almacanamiento sera un valor
        #de tipo entero
        precio_compra = float(input("Precio de compra del dispositivo: "))#float por que el precio ee
        #un valor de tipo decimal en muchos casos

        dispositivo = DispositivoElectronico(tipo, modelo, procesador, memoria, almacenamiento, precio_compra)
        dispositivos.append(dispositivo)

    return dispositivos
    #utilizaremos el return para que devuelva los valores correspondiendes introducidos por el usuario

# Función para mostrar información de los dispositivos
#imprimira en pantalla los datos de los dispositivos junto a la informacion de su venta
def mostrar_dispositivos(dispositivos):
    for dispositivo in dispositivos:
        dispositivo.mostrar_informacion()
        print("-" * 30)

# Ejemplo de uso
dispositivos = registrar_dispositivos()
mostrar_dispositivos(dispositivos)
