# Aplicações de Python na Termodinâmica para Engenharia Química

####  ***Maiara de Souza Salmaso***

## Exercícios 
**Resolvendo sistema de equações lineares**

## Coluna de destilação para separação de metano, etano e propano.

- Diagrama de uma coluna de destilação para separação grosseira de Metano (M), Etano (E) e Propano (P). Separação de fases por componentes.

- Como bem sabemos, a destilação tem a ver com diferentes pontos de ebulição e mais especificamente com a diferença nas volatilidades relativas.

A partir dos dados fornecidos podemos propor um balanço material.


***balanço material***

$$m_{entrada} = m_{saída}$$

$$30 kg/s = 0,9m_{1} + 0,3m_{2} + 0,1m_{3}$$

$$25 kg/s = 0,1m_{1} + 0,5m_{2} + 0,2m_{3}$$

$$10 kg/s = 0,0m_{1} + 0,2m_{2} + 0,7m_{3}$$


Temos um sistema de equações que poderíamos muito bem resolver com alguns dos muitos métodos que aprendemos (ou aprenderemos) ao longo do curso. Porém, resolveremos este problema de sistemas de equações lineares em Python maneira analítica.

![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/10970fc6-ac53-4080-9bdc-dc3851453c4b)


  A primeira coisa que faremos é **instalar as bibliotecas** , usaremos `sympy` para trabalhar com símbolos
  Basta abrir o promt de comando de seu computador e digitar pip install (nome da biblioteca) - **sem parenteses**
  Lembremos que para importar uma biblioteca é necessário utilizar o comando `pip install + nomes de bibliotecas´.

Em seguida para importá-las, é necessário utilizar o comando `import + nomes de bibliotecas`. logo no início de seu projeto.

import scipy

#### Declarar as variáveis como símbolos*

`m1, m2, m3 = sympy.symbols('m1 m2 m3')`

#### Definindo as equações 

`eq1 = 0.9*m1 + 0.3*m2 + 0.1*m3 - 30`

`eq2 = 0.1*m1 + 0.5*m2 + 0.2*m3 - 25`

`eq3 = 0.2*m2 + 0.7*m3 - 10`

#### Resolvendo o sistema
`solução = sympy.solve([eq1,eq2,eq3],[m1,m2,m3])`

#### Imprimindo (ou retornando) os resultados
`print(solução[m1])`

`print(solução[m2])`

`print(solução[m3])` 

você retornará todas variáveis do problema

![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/880ea6c1-6b65-42cf-a2ef-b76355572e5b)


# Introdução às bibliotecas

## Interpolação & Tbaelas de Vapor

  Interpolação é um método matemático utilizado para estimar valores desconhecidos que se situam entre dois valores conhecidos em uma sequência de dados. No contexto da engenharia termodinâmica, a interpolação é frequentemente utilizada para encontrar propriedades de substâncias como vapor e água a determinadas condições de pressão e temperatura.
* ####  Método Numérico
  A equação básica da interpolação linear é:
  
![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/408928d0-e941-49ea-b5ce-a9608810cd67)

Para resolvê-la, basta ir à uma tabela, retirar os dados dos pontos x e y e substituir na equação acima. Calculadoras Gráficas como a HP Prime, ou a HP 50G possuem esta função de interpolação de forma "nativa" em suas aplicaçõas, mas caso naão tenha uma, basta utilizar este algoritmo.

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

:yellow_circle:`Caso tenha interesse, este algoritmo foi desenvolvido com uma interface gráfica de usuário e está disponível neste repositório!`

#### Mas onde entram as bibliotecas termodinâmicas? E como encontrá-las?


<img src="https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/99560f6c-db20-4b16-814d-878ec768ba94" alt="Image Description" width="300"/>

## Equações de Estado
