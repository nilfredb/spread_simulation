import numpy as np


#Aqui intentare definir el tipo de dimension de la matriz

# 0 para sano, 1 para infectado, 2 para desconocido


# Vecindarios ----------------------------------------

#standard
matrix = np.array([[0, 0, 0],
                   [1, 0, 0],
                   [0, 0, 0]])


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

matrix_choise = matrix_2  # Por defecto, elegimos la matriz de alta probabilidad
print(f"Matriz por defecto: \n{matrix_choise}")


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


# Definicion base de lo que intento hacer.
# Esto es un sistema 1d de estado, quiere decir que 1 es si y 0 es no, para si es infectado y para no es sano, 
# Por lo que puede verlo como un total de 9 personas en un espacio, y cada persona puede estar infectada o sana,
# por lo que el sistema tiene 2^9 estados posibles, es decir, 512 estados posibles.

# Funciones

#Funcion que toma los argumentos del tamano de la matriz y la crea, generando un estado positivo en infeccion aleatorio
# def generate_matrix(x: int, y: int) -> np.ndarray:
#     matrix = np.zeros((x, y), dtype=object)
#     return matrix

# Esta infecta con su posicion indicada
def infectar_persona(matrix: np.ndarray, x: int, y: int) -> np.ndarray:
    matrix[x][y] = 1
    return matrix

# Funcion para infectar aleatoriamente una persona en la matriz
def infectar_aleatorio (matrix: Mundo) -> Mundo:
    i = np.random.randint(0, matrix.matrix.shape[0])
    j = np.random.randint(0, matrix.matrix.shape[1])
    matrix.matrix[i][j] = 1
    return matrix

# Obtener vecinos

def obtener_vecinos(matrix: np.ndarray, x: int, y: int) -> list:
    vecinos = []
    for i in range(max(0, x - 1), min(matrix.shape[0], x + 2)):
        for j in range(max(0, y - 1), min(matrix.shape[1], y + 2)):
            if (i, j) != (x, y):
                vecinos.append((i, j))
    return vecinos

# Regla de determinacion por vecino cercano, si hay alguien al lado lo infecta
def simulacion_propagacion(matrix: np.ndarray) -> np.ndarray:
    matriz_nueva = matrix.copy()
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[x][y] == 1:
                for i, j in obtener_vecinos(matrix, x, y):
                    matriz_nueva[i][j] = 1
    return matriz_nueva

# Regla basada en probabilidad, si hay alguien al lado, hay una probabilidad x de probabilidad de infectar

def simulacion_propagacion_probabilistica(matrix: np.ndarray, probabilidad: float) -> np.ndarray:
    if 0 <= probabilidad <= 1:
        matrix = simulacion_propagacion_probabilistica(matrix, probabilidad)
    else:
        print("La probabilidad debe estar entre 0 y 1.")
    matriz_nueva = matrix.copy()
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[x][y] == 1:
                for i, j in obtener_vecinos(matrix, x, y):
                    if np.random.rand() < probabilidad:
                        matriz_nueva[i][j] = 1
    return matriz_nueva

#Funcion para contar los infectados
def contar_infectados(matrix) -> int:
    return np.sum(matrix)
#Funcion para contar los sanos
def contar_sanos(matrix) -> int:
    return matrix.size - np.sum(matrix)

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
        x_1, y_1 = int(input('Elige la dimension del eje x(solo numeros): ')), int(input('Elige la dimension del eje y(solo numeros): '))
        matrix = Mundo(x_1, y_1)
        print(f"Matriz generada: \n{matrix.matrix}")
        agente = input("Generar infectado aleatorio? ")
        if agente == "si":
            matrix = infectar_aleatorio(matrix)
            print(f"Matriz con infectado aleatorio en : \n{matrix.matrix}")
        print(f"Matriz de {x_1}x{y_1} generada, el total de infectados es de: {contar_infectados(matrix.matrix)} ubicado en la posicion: {np.argwhere(matrix.matrix == 1)}")

    elif menu == "1":
        x, y = int(input('Elige la posicion del eje x para infectar(solo numeros): ')), int(input('Elige la posicion del eje y para infectar(solo numeros): '))
        if 0 <= x < matrix.shape[0] and 0 <= y < matrix.shape[1]:
            infectar_persona(matrix, x, y)
            print(f"Persona infectada en la posicion ({x}, {y}): \n{matrix}")
        else:
            print("Coordenadas fuera de rango.")
    elif menu == "2":
        print(f"Total de infectados: {contar_infectados(matrix)}")
        print(f"Total de sanos: {contar_sanos(matrix)}")
    elif menu == "3":
        tipo_propagacion = input("Elige el tipo de propagacion: 1) Vecino cercano, 2) Probabilistica -> ")
        if tipo_propagacion == "1":
            matrix = simulacion_propagacion(matrix)
        elif tipo_propagacion == "2":
            probabilidad = float(input("Elige la probabilidad de infeccion (0-1) / Float valido: "))
            matrix = simulacion_propagacion_probabilistica(matrix, probabilidad)
        print(matrix)
    elif menu == "4":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")






