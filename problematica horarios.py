# Este programa ayuda a los estudiantes de la Universidad Gerardo Barrios a gestionar sus horarios 
# de clases y entrenamientos, identificando y sugiriendo soluciones a los conflictos de horarios, 
# lo que facilita la asistencia a ambos.

#definitos la clase "estudiante"
class Estudiante:
    #la inicializamos junto a los atributos de la clase
    def __init__(self, nombre):#aqui iran los datos de los estudiantes
        self.nombre = nombre
        self.horarios_clases = []
        self.horarios_entrenos = []
    #utilizaremos multiples metodos para agregar los horarios y veriifcar si hay conflictos entre ellos
    #aqui agreramos los horarios de clases de las materias
    def agregar_horario_clase(self, dia, hora_inicio, hora_fin):
        self.horarios_clases.append((dia, hora_inicio, hora_fin))
    #aqui agregaremos los horarios de los clubes de entreno
    def agregar_horario_entreno(self, deporte, dia, hora_inicio, hora_fin):
        self.horarios_entrenos.append((deporte, dia, hora_inicio, hora_fin))
    #verigicara aqui el programa si hay choques o no entre ellos 
    def verificar_conflictos(self):
        conflictos = []
        for clase in self.horarios_clases:
            for entreno in self.horarios_entrenos:
                if clase[0] == entreno[1] and not (clase[2] <= entreno[2] or clase[1] >= entreno[3]):
                    conflictos.append((clase, entreno))
                    #devolvera los datos en caso de conflictos 
        return conflictos
#aca comenzaremos a introducir los datos en las variables
def main():
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiante = Estudiante(nombre)
#emperazemos a utilizar un ciclo while para que evalue si se cumplen las condiciones 
    while True:
        #introduciremos los datos de los horarios 
        opcion = input("¿Desea agregar un horario de clase o entreno? (clase/entreno/salir): ")
        if opcion == "clase":
            dia = input("Ingrese el día de la clase: ")
            hora_inicio = input("Ingrese la hora de inicio de la clase (HH:MM): ")
            hora_fin = input("Ingrese la hora de fin de la clase (HH:MM): ")
            estudiante.agregar_horario_clase(dia, hora_inicio, hora_fin)
            #utilizaremos un elif ya que estamos evaluando multiples horarios 
        elif opcion == "entreno":
            deporte = input("Ingrese el deporte del entreno: ")
            dia = input("Ingrese el día del entreno: ")
            hora_inicio = input("Ingrese la hora de inicio del entreno (HH:MM): ")
            hora_fin = input("Ingrese la hora de fin del entreno (HH:MM): ")
            estudiante.agregar_horario_entreno(deporte, dia, hora_inicio, hora_fin)
            #utilizaremos un elif para salir del bucle
        elif opcion == "salir":
            break#el break se encargara de cerrar el bucle al seleccion "salir"
            #aca encontrara si hubo conflictos o choques entre los horarios 
    conflictos = estudiante.verificar_conflictos()
    if conflictos:
        print("Conflictos encontrados:")
        for clase, entreno in conflictos:
            print(f"Clase: {clase} - Entreno: {entreno}")
    else:
        print("No se encontraron conflictos.")#en caso que no hayan conflictos mostrara en pantalla esto

if __name__ == "__main__":
    main()
