import numpy as np
from scipy.optimize import fsolve

# Função de Van der Waals
def van_der_waals(V, P, n, T, a, b, R=0.0821):
    return P + a * (n / V)**2 * (V - n * b) - n * R * T / V

# Função para resolver a equação de Van der Waals e retornar o volume
def solve_van_der_waals(P, n, T, a, b, V_guess=1.0):
    # Definir a função de resíduo
    residual_func = lambda V: van_der_waals(V, P, n, T, a, b)
    
    # Resolver a equação de Van der Waals para encontrar o volume
    V_solution = fsolve(residual_func, V_guess)[0]
    
    return V_solution

# Exemplo de uso:
P = 10.0  # Pressão específica em atm
T = 300.0  # Temperatura em K
n = 1.0  # Quantidade de substância em mol
a = 1.36  # Constante específica para o gás
b = 0.0318  # Constante específica para o gás

# Resolver a equação de Van der Waals para encontrar o volume
V = solve_van_der_waals(P, n, T, a, b)
print(f"O volume para é  P = {P} atm: {V:.4f} L")
