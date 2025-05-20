import sympy

# Declarar as variáveis
m1, m2, m3 = sympy.symbols('m1 m2 m3')

# Definir as equações
eq1 = 0.9*m1 + 0.3*m2 + 0.1*m3 - 30
eq2 = 0.1*m1 + 0.5*m2 + 0.2*m3 - 25
eq3 = 0.2*m2 + 0.7*m3 - 10

# Resolver o sistema de equações
solucao = sympy.solve([eq1, eq2, eq3], [m1, m2, m3])

# Imprimir os resultados
print(solucao[m1])
print(solucao[m2])
print(solucao[m3])
