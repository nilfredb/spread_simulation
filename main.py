import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]])

print(matrix)


# Definicion base de lo que intento hacer.
# Esto es un sistema 1d de estado, quiere decir que 1 es si y 0 es no, para si es infectado y para no es sano, 
# Por lo que puede verlo como un total de 9 personas en un espacio, y cada persona puede estar infectada o sana,
# por lo que el sistema tiene 2^9 estados posibles, es decir, 512 estados posibles.

# Funciones

# Esta nos devuelve el sano
def sano(matrix):
    return np.sum(matrix) == 0

# esta nos devuelve el infectado
def infectado(matrix):
    return np.sum(matrix) > 0

# Esta infecta con su posicion
def infectar_persona(matrix, x, y):
    infectar = input("Infectar? ")
    if infectar == "si":
        matrix[x][y] = 1
        print(matrix)
    elif infectar == "no":
        matrix[x][y] = 0
        print(matrix)
    else:
        print("Opcion no valida")


# Clases
# Esta clase representa el sistema, y tiene un metodo que devuelve el estado del sistema, ya sea sano, infectado o desconocido, dependiendo de la matriz que se le pase.
class Sistema:
    def __init__(self, matrix):
        self.matrix = matrix

    def estado(self):
        if sano(self.matrix):
            return "Sano"
        elif infectado(self.matrix):
            return "Infectado"
        else:
            return "Desconocido"



# Persona seran los elementos de la matriz, o sea 9
class persona:
    def __init__(self, estado, matrix, x, y):
        self.estado = estado
        self.matrix = matrix
        self.x = x
        self.y = y

    def infectar(self):
        self.estado = 1

    def sanar(self):
        self.estado = 0