class Perro: #definiremos la clase
    #init inicializara la clase junto a sus atributos 
    def __init__(self, nombre, raza, edad, peso, color, dueño, telefono): #aca definiremos los datos de las caracteristicas
        #procederemos a poner las caracteristicas de los perros
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.telefono = telefono
        self.estado = "NO ATENDIDO" #recordar que los perros no registrados tendran el estado de "NO ATENDIDO"
        self.tamaño = "perro grande" if peso >= 10 else "perro pequeño"
        #el tamaño lo clasifica conforme al peso del perro 
    
    def registrar(self):
        self.estado = "ATENDIDO"
        #aqui una vez registrados los datos pasara a ser "ATENDIDO"
    
    def mostrar_informacion(self):
        #usaremos este metodo para mostrar la informacion 
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Dueño: {self.dueño}")
        print(f"Teléfono: {self.telefono}")
        print(f"Estado: {self.estado}")
        print(f"Tamaño: {self.tamaño}")
        

# Ejemplo de uso
#aqui introduciremos los datos de los perros 
nombre = input("Nombre del perro: ")
raza = input("Raza del perro: ")
edad = int(input("Edad del perro: "))#la edad es un caracter de tipo entero
peso = float(input("Peso del perro (kg): "))#float por que el peso es un caracter en muchas ocasiones decimal
color = input("Color del perro: ")
dueño = input("Nombre del dueño: ")
telefono = input("Teléfono del dueño: ")


perro = Perro(nombre, raza, edad, peso, color, dueño, telefono)
perro.registrar()
perro.mostrar_informacion()
