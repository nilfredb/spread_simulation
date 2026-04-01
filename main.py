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

def sano(matrix):
    return np.sum(matrix) == 0


def infectado(matrix):
    return np.sum(matrix) > 0


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


infectar = input("Infectar? ")
if infectar == "si":
    matrix[0][0] = 1
    print(matrix)
elif infectar == "no":
    matrix[0][0] = 0
    print(matrix)
else:
    print("Opcion no valida")

# Persona seran los elementos de la matriz, o sea 9
class persona:
    def __init__(self, estado):
        self.estado = estado

    def infectar(self):
        self.estado = 1

    def sanar(self):
        self.estado = 0