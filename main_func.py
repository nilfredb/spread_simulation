import numpy as np
mundo = None # Universo 0
#Aqui intentare definir el tipo de dimension de la matriz

# 0 para sano, 1 para infectado, 2 para desconocido


# Vecindarios ----------------------------------------

#standard
# matrix = np.array([[0, 0, 0],
#                    [1, 0, 0],
#                    [0, 0, 0]])


# Alta probabilidad
matrix_2 = np.array(
                    [
                    [1, 1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1]])

#baja probabilidad
matrix_3 = np.array([[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 1]])




# Clases

# Estados: 0 para sano, 1 para infectado, 2 para desconocido

# Persona seran los elementos de la matriz, o sea 9
class Persona:
    def __init__(self, name: str, x: int, y: int, edad = None, estado = None):
        self.name = "PACIENTE_0"
        self.x = x
        self.y = y
        self.edad = edad
        self.estado = estado

class Infeccion:
    def __init__(self, tipo: str, probabilidad: float):
        self.tipo = tipo
        self.probabilidad = probabilidad

class Mundo:
    def __init__(self, x, y):
        self.matrix = np.zeros((x, y), dtype=int)
    # Migracion de funciones a la clase Mundo
    # Empezare por las mas faciles
    #Funcion para contar los infectados y sanos
    def contar_infectados(self) -> int:
        return np.sum(self.matrix)

    def contar_sanos(self) -> int:
        return self.matrix.size - np.sum(self.matrix)

    # Obtener vecinos

    def obtener_vecinos(self, x: int, y: int) -> list:
        vecinos = []
        for i in range(max(0, x - 1), min(self.matrix.shape[0], x + 2)):
            for j in range(max(0, y - 1), min(self.matrix.shape[1], y + 2)):
                if (i, j) != (x, y):
                    vecinos.append((i, j))
        return vecinos

    # Vamos con los cambios de estado

    # Esta infecta con su posicion indicada
    def infectar_persona(self, x: int, y: int) -> None:
        if self.matrix[x][y] == 0:
            self.matrix[x][y] = 1
            print("Agente infectado con exito.")
        else:
            print("Este agente ya esta infectado.")

# Funcion para infectar aleatoriamente una persona en la matriz
    def infectar_aleatorio (self):
        i = np.random.randint(0, self.matrix.shape[0])
        j = np.random.randint(0, self.matrix.shape[1])
        self.matrix[i][j] = 1
        # Regla de determinacion por vecino cercano, si hay alguien al lado lo infecta
    def simulacion_propagacion(self) -> np.ndarray:
        matriz_nueva = self.matrix.copy()
        for x in range(self.matrix.shape[0]):
            for y in range(self.matrix.shape[1]):
                if self.matrix[x][y] == 1:
                    for i, j in self.obtener_vecinos(x, y):
                        matriz_nueva[i][j] = 1
        return matriz_nueva
    # Regla basada en probabilidad, si hay alguien al lado, hay una probabilidad x de probabilidad de infectar

    def simulacion_propagacion_probabilistica(self, probabilidad: float) -> np.ndarray:
        if 0 <= probabilidad <= 1:
            print('Probabilidad valida, simulando propagacion...')
        else:
            print("La probabilidad debe estar entre 0 y 1.")
            self.simulacion_propagacion_probabilistica(float(input("Elige la probabilidad de infeccion (0-1) / Float valido: ")))
        matriz_nueva = self.matrix.copy()
        for x in range(self.matrix.shape[0]):
            for y in range(self.matrix.shape[1]):
                if self.matrix[x][y] == 1:
                    for i, j in self.obtener_vecinos(x, y):
                        if np.random.rand() < probabilidad:
                            matriz_nueva[i][j] = 1
        return matriz_nueva


# Definicion base de lo que intento hacer.
# Esto es un sistema 1d de estado, quiere decir que 1 es si y 0 es no, para si es infectado y para no es sano,
# Por lo que puede verlo como un total de 9 personas en un espacio, y cada persona puede estar infectada o sana,
# por lo que el sistema tiene 2^9 estados posibles, es decir, 512 estados posibles.

# Funciones

#Funcion que toma los argumentos del tamano de la matriz y la crea, generando un estado positivo en infeccion aleatorio
# def generate_matrix(x: int, y: int) -> np.ndarray:
#     matrix = np.zeros((x, y), dtype=object)
#     return matrix








def default_matrix():
    mundo = Mundo(9, 9)
    return mundo.matrix
if mundo is None:
    mundo = default_matrix()

print(f"Matriz por defecto: \n{mundo}")

# Funcion para lanzar agente infeccioso, que se encargara de infect

# Pensamientos: para simular correctamente necesito reglas de infeccion, es decir que valores la funcion verificara para saber
#cuando y donde infectar
#-----



while True:
    menu = input("""
    0-) Generar matriz custom
    1-) Infectar persona
    2-) Ver total de enfermos y sanos
    3-) Simular propagacion
    4-) Salir

                 -> """)


    if menu == "0":
        # Aqui se vuelve a definir la variable matrix usando la funcion de la clase (Ya no es None)
        x_1, y_1 = int(input('Elige la dimension del eje x(solo numeros): ')), int(input('Elige la dimension del eje y(solo numeros): '))
        mundo = Mundo(x_1, y_1) # Mundo principal, universo 1
        print(f"Matriz generada: \n{mundo.matrix}")
        agente = input("Generar infectado aleatorio? ")
        if agente == "si":
            mundo.infectar_aleatorio() # Mundo infectado, universo 2, con un infectado aleatorio
            print(f"Matriz con infectado aleatorio en : \n{mundo.matrix}")
        print(f"Matriz de {x_1}x{y_1} generada, el total de infectados es de: {mundo.contar_infectados()} ubicado en la posicion: {np.argwhere(mundo.matrix == 1)}")

    elif menu == "1":
        x, y = int(input('Elige la posicion del eje x para infectar(solo numeros): ')), int(input('Elige la posicion del eje y para infectar(solo numeros): '))
        if 0 <= x < mundo.matrix.shape[0] and 0 <= y < mundo.matrix.shape[1]:
            mundo.infectar_persona(x, y)
            print(f"Persona infectada en la posicion ({x}, {y}): \n{mundo.matrix}")
        else:
            print("Coordenadas fuera de rango.")
    elif menu == "2":
        print(f"Total de infectados: {mundo.contar_infectados()}")
        print(f"Total de sanos: {mundo.contar_sanos()}")
    elif menu == "3":
        tipo_propagacion = input("Elige el tipo de propagacion: 1) Vecino cercano, 2) Probabilistica -> ")
        if tipo_propagacion == "1":
            mundo_nuevo = mundo.simulacion_propagacion()
        elif tipo_propagacion == "2":
            probabilidad = float(input("Elige la probabilidad de infeccion (0-1) / Float valido: "))
            mundo_nuevo = mundo.simulacion_propagacion_probabilistica(probabilidad)
        print(mundo_nuevo)
    elif menu == "4":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")

