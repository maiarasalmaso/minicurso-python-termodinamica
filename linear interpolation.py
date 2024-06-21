import tkinter as tk

def calcular_interp_linear():
    # Obtém os valores de x e y inseridos pelo usuário
    x_valores = [float(x_entry.get()) for x_entry in x_entries]
    y_valores = [float(y_entry.get()) for y_entry in y_entries]

    # Obtém o valor de x para o qual a interpolação será calculada
    valor_x = float(valor_x_entry.get())

    # Calcula a interpolação linear
    resultado = interpolar(x_valores, y_valores, valor_x)

    # Exibe o resultado na etiqueta de saída
    resultado_label.config(text=f"Resultado da interpolação linear: {resultado}")

def interpolar(x_valores, y_valores, valor_x):
    if len(x_valores) != 2 or len(y_valores) != 2:
        return "Por favor, insira exatamente 2 pontos de dados (x, y)."

    x1, x2 = x_valores
    y1, y2 = y_valores

    # Calcula a interpolação linear
    resultado = y1 + ((valor_x - x1) * (y2 - y1)) / (x2 - x1)
    return resultado

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Interpolação Linear Simples")

# Cria rótulos e campos de entrada para valores de x e y
tk.Label(janela, text="Valores de x").grid(row=0, column=0)
tk.Label(janela, text="Valores de y").grid(row=0, column=2)

x_entries = []
y_entries = []

for i in range(2):
    tk.Label(janela, text=f"x{i + 1}:").grid(row=i + 1, column=0)
    x_entry = tk.Entry(janela)
    x_entry.grid(row=i + 1, column=1)
    x_entries.append(x_entry)

    tk.Label(janela, text=f"y{i + 1}:").grid(row=i + 1, column=2)
    y_entry = tk.Entry(janela)
    y_entry.grid(row=i + 1, column=3)
    y_entries.append(y_entry)

# Campo de entrada para o valor de x para interpolação
tk.Label(janela, text="Valor de x para interpolação:").grid(row=3, column=0)
valor_x_entry = tk.Entry(janela)
valor_x_entry.grid(row=3, column=1)

# Botão para calcular a interpolação linear
calcular_button = tk.Button(janela, text="Calcular", command=calcular_interp_linear)
calcular_button.grid(row=4, column=0, columnspan=4)

# Etiqueta para exibir o resultado
resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
resultado_label.grid(row=5, column=0, columnspan=4)

# Inicia a interface gráfica
janela.mainloop()
