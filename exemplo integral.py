from sympy import Symbol, integrate

# Definindo a variável simbólica 'x'
x = Symbol('x')

# Definindo a função para a qual queremos calcular a integral
funcao = x**2 + 3*x + 2

# Calculando a integral de 'expr' em relação a 'x'
integral = integrate(funcao, x)

# Mostrando o resultado da integral
print(integral)
