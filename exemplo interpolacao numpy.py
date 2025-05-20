import numpy as np

def calcular_interp_linear():
    # Obtém os valores de x e y inseridos pelo usuário
    x_valores = []
    y_valores = []

    for i in range(2):
        x_valor = float(input(f"Digite o valor de x{i + 1}: "))
        x_valores.append(x_valor)

        y_valor = float(input(f"Digite o valor de y{i + 1}: "))
        y_valores.append(y_valor)

    # Obtém o valor de x para o qual a interpolação será calculada
    valor_x = float(input("Digite o valor de x para interpolação: "))

    # Calcula a interpolação linear usando numpy
    resultado = np.interp(valor_x, x_valores, y_valores)

    # Exibe o resultado
    print(f"Resultado da interpolação linear: {resultado}")

# Chama a função para calcular a interpolação
calcular_interp_linear()
