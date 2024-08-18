#defininimos la clase
class Auto:
    #inicializamos la clase 
    def __init__(self, marca, modelo, año, color, tipo_combustible, cilindrada, transmision, precio_compra, origen, kilometraje):
        #definiremos los atributos de la clase para que el init los inicie 
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_combustible = tipo_combustible
        self.cilindrada = cilindrada
        self.transmision = transmision
        self.precio_compra = precio_compra
        self.origen = origen
        self.kilometraje = kilometraje
        self.ruedas = 4 #recordar que solo seran vehiculos de 4 ruedas
        self.capacidad_pasajeros = 5 #la capacidad maxima de todos los vehiculas a registrar sera de 5 pajaseros
        self.precio_venta = precio_compra * 1.4 #recordar que el precio se multiplica por 1.4 
        #el resultado sera la ganancia de nuestra venta

    def mostrar_informacion(self):
        #procedemos a utilizar este metodo para mostrar la informacion en pantalla de los autos 
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de combustible: {self.tipo_combustible}")
        print(f"Cilindrada: {self.cilindrada} cc")
        print(f"Transmisión: {self.transmision}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Origen: {self.origen}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

# Función para registrar autos
def registrar_autos():
    autos = []
    #utilizaremos un for para ejecutar mas de dos veces este metodo 
    for _ in range(2):  # Registrar al menos dos autos
        marca = input("Marca del auto: ")
        modelo = input("Modelo del auto: ")
        año = int(input("Año del auto: "))#el año sera un valor de tipo entero
        color = input("Color del auto: ")
        tipo_combustible = input("Tipo de combustible del auto: ")
        cilindrada = int(input("Cilindrada del auto (cc): ")) #los cilindros seran un valor de tipo entero
        transmision = input("Transmisión del auto (manual/automática): ")
        precio_compra = float(input("Precio de compra del auto: "))#el precio sera un valor de tipo decimal
        origen = input("Origen del auto (nacional/importado): ")
        kilometraje = int(input("Kilometraje del auto: "))#el kilomatraje sera un valor de tipo entero 

        auto = Auto(marca, modelo, año, color, tipo_combustible, cilindrada, transmision, precio_compra, origen, kilometraje)
        autos.append(auto)

    return autos
    #devolvera la informacion introducida por el usuario 

# Función para mostrar información de los autos
#mostrara todas las caracteristicas del auto mas el precio de la venta 
def mostrar_autos(autos):
    for auto in autos:
        auto.mostrar_informacion()
        print("-" * 30)

# Ejemplo de uso
autos = registrar_autos()
mostrar_autos(autos)
