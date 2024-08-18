#definimos la clase
class Articulo:
    #init para inicializar la clase junto a sus atributos
    def __init__(self, tipo, especificacion, precio_compra):#las variables conforme al tipo de producto, especificacion y su precio
        self.tipo = tipo
        self.especificacion = especificacion
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30 #recordar que el precio se multiplica por 1,30
        #el resultado sera la ganancia de la venta

    def mostrar_informacion(self):
        #usaremos este metodo para mostrar en pantalla ia informacion de los lapicez y los cuadernos 
        print(f"Tipo: {self.tipo}")
        print(f"Especificación: {self.especificacion}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

# Función para registrar artículos(lapicez o cuadernos)
def registrar_articulos():
    articulos = []

    for _ in range(2):  # Registrar al menos dos artículos de cada tipo (cuaderno)
        tipo = "Cuaderno"
        especificacion = input("Especificación del cuaderno (50 o 100 hojas): ")
        precio_compra = float(input("Precio de compra del cuaderno: "))
        cuaderno = Articulo(tipo, f"{especificacion} hojas, marca HOJITAS", precio_compra)
        articulos.append(cuaderno)

    for _ in range(2):  # Registrar al menos dos artículos de cada tipo(lapicez)
        tipo = "Lápiz"
        especificacion = input("Especificación del lápiz (grafito o colores): ")
        precio_compra = float(input("Precio de compra del lápiz: "))
        lapiz = Articulo(tipo, f"{especificacion}, marca RAYAS", precio_compra)
        articulos.append(lapiz)

    return articulos

# Función para mostrar información de los artículos
#aqui imprimeremos en pantalla la informacion de los productos registrados junto con la gannacia de venta
def mostrar_articulos(articulos):
    for articulo in articulos:
        articulo.mostrar_informacion()
        print("-" * 30)

# Ejemplo de uso
articulos = registrar_articulos()
mostrar_articulos(articulos)
