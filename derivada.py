import sympy as sp

# Definir a variável
x = sp.symbols('x')

# Definir a função
f = 3*x**4 - 5*x**3 + 2*x - 7

# Calcular a derivada
derivada = sp.diff(f, x)

# Exibir a derivada
print(derivada)
