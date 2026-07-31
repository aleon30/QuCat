import math
import random

# Representación interna de un qubit: vector de dos números complejos [alpha, beta]
# |0> es [1.0, 0.0] y |1> es [0.0, 1.0]

def qubit_inicial(estado='0'):
    if estado == '1':
        return [0.0 + 0j, 1.0 + 0j]
    return [1.0 + 0j, 0.0 + 0j]

# Definición de las matrices de las compuertas cuánticas
INV_SQRT2 = 1.0 / math.sqrt(2)

COMPUERTAS = {
    "H": [[INV_SQRT2, INV_SQRT2], 
          [INV_SQRT2, -INV_SQRT2]],
    "X": [[0, 1], 
          [1, 0]],
    "Y": [[0, -1j], 
          [1j, 0]],
    "Z": [[1, 0], 
          [0, -1]],
    "S": [[1, 0], 
          [0, 1j]],
    "T": [[1, 0], 
          [0, math.cos(math.pi/4) + 1j * math.sin(math.pi/4)]]
}

def aplicar_compuerta(qubit, compuerta):
    if compuerta not in COMPUERTAS:
        return qubit
    
    matrix = COMPUERTAS[compuerta]
    # Multiplicación matriz-vector: M * [a, b]
    a_new = matrix[0][0] * qubit[0] + matrix[0][1] * qubit[1]
    b_new = matrix[1][0] * qubit[0] + matrix[1][1] * qubit[1]
    
    return [a_new, b_new]

def qubit_actual(qubit, compuerta):
    return aplicar_compuerta(qubit, compuerta)

def colapsar_qubit(qubit):
    # Calcula la probabilidad P(0) = |alpha|^2
    prob_0 = abs(qubit[0]) ** 2
    
    # Colapso aleatorio según la probabilidad
    if random.random() < prob_0:
        return '0'
    else:
        return '1'