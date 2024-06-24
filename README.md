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

<img src="https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/10970fc6-ac53-4080-9bdc-dc3851453c4b" alt="Image Description" width="300"/>

  A primeira coisa que faremos é **instalar as bibliotecas** , usaremos `sympy` para trabalhar com símbolos
  Basta abrir o promt de comando de seu computador e digitar pip install (nome da biblioteca) - **sem parenteses**
  Lembremos que para importar uma biblioteca é necessário utilizar o comando `pip install + nomes de bibliotecas´.

Em seguida para importá-las, é necessário utilizar o comando `import + nomes de bibliotecas`. logo no início de seu projeto.

import scipy

#### Declarar as variáveis como símbolos*

        m1, m2, m3 = sympy.symbols('m1 m2 m3')

#### Definindo as equações 

        eq1 = 0.9*m1 + 0.3*m2 + 0.1*m3 - 30

        eq2 = 0.1*m1 + 0.5*m2 + 0.2*m3 - 25

        eq3 = 0.2*m2 + 0.7*m3 - 10

#### Resolvendo o sistema
          solução = sympy.solve([eq1,eq2,eq3],[m1,m2,m3])

  #### Imprimindo (ou retornando) os resultados
          print(solução[m1])

          print(solução[m2])

          print(solução[m3])

você retornará todas variáveis do problema

![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/880ea6c1-6b65-42cf-a2ef-b76355572e5b)


# Introdução às bibliotecas

## Interpolação & Tbaelas de Vapor

  Interpolação é um método matemático utilizado para estimar valores desconhecidos que se situam entre dois valores conhecidos em uma sequência de dados. No contexto da termodinâmica, a interpolação é frequentemente utilizada para encontrar propriedades de substâncias como vapor e água em determinadas condições de pressão e temperatura.
  
* ####  Método Numérico
  A equação básica da interpolação linear é:
  
![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/408928d0-e941-49ea-b5ce-a9608810cd67)

Para resolver isso, basta consultar uma tabela, extrair os dados dos pontos x e y e substituí-los na equação acima. Calculadoras gráficas como a HP Prime ou a HP 50G possuem essa função de interpolação de forma nativa em suas aplicações, mas caso não tenha uma, basta utilizar este algoritmo.


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

Neste mesmo site, você pode encontrar uma infinidade de bibliotecas open-source! Basta clicar na lupa, como na imagem abaixo, e digitar o assunto desejado, preferencialmente em inglês

![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/74bbeb34-ccfe-49a8-a9a1-8ad906683c7b)

Como nosso foco é termodinâmica e propriedades de água saturada, podemos simplesmennte buscar por `Thermodynamic properties`

## Propriedades da água

Para propriedades de saturação  a melhor opção de bibliotecas foi a [pyXSteam]([https://github.com/KurtJacobson/XSteam](https://pypi.org/project/pyXSteam/)), cuja documentação, é baseada em dados da [IAPWS](http://iapws.org/) (Associação Internacional de Propriedades de Água e Vapor) logo é utilizada apenas para dados de água, que será o nosso foco!

`Para instalar, basta copiar o pip install presente em seu repositório disponível no link`

:red_circle: **Exemplo para determinar o volume da água no estado líquido para 50ºC**

        from pyXSteam.XSteam import XSteam
        steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS)
        print(steamTable.vV_t(50))

:red_circle: **Volume em função da pressão e temperatura.**

        from pyXSteam.XSteam import XSteam
        steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS)
        print(steamTable.v_pt(20,10))


##  Equações de Estado

As equações de estado termodinâmicas são expressões matemáticas que relacionam variáveis termodinâmicas de um sistema, como pressão (P), volume (V), temperatura (T) e quantidade de substância (n). Elas são essenciais para descrever o comportamento dos gases e líquidos em diferentes condições.

![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/7a9058f3-e3ca-46c4-9177-160410299f34)

**Por ser mais simples de se cálcular, para este exemplo itremos utilizar a equação de Van Der Waals para calcular o Volume de um gás em uma determinada temperatura**

![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/f07a6fd5-71b8-43fd-8b49-aa69d09a8a4f)
![image](https://github.com/maiarasalmaso/minicurso-python-termodinamica/assets/91421583/c2666ccd-b067-4cd3-abcb-dbedc75dbd35)

Obs: Pr = P/Pc e Tr = T/Tc

🟢**Solução analítica**
Solução analítica: Este cálculo, por se tratar de uma equação de estado cúbica, convém ser solucionado por meio de uma calculadora gráfica, Excel ou Python
       
        import numpy as np
        from scipy.optimize import fsolve
        
        # Funçãoo de Van der Waals
        def van_der_waals(V, P, n, T, a, b, R=0.0821):
        return P + a * (n / V)**2 * (V - n * b) - n * R * T / V

        # Funçãoo para resolver a equação de Van der Waals e retornar o volume
        def solve_van_der_waals(P, n, T, a, b, V_guess=1.0):
        # Definir a função de resÃ­duo
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
        print(f"O volume para Ã©  P = {P} atm: {V:.4f} L")

Fazendo uma nova pesquisa por bibliotecas, é possível encontrar a biblioteca [CoolProp](https://github.com/CoolProp/CoolProp) desenvoldida em C++. Em seu repositório é disponibilizado toda sua [documentação](http://coolprop.org/), onde é possível encontrar diversas dicas de como utilizar 


Veja que com a utilização desta biblioteca, utilizamos apenas três linhas de código para encontrar a temperatura do propano a 1 atm ou 101325 Pa

        import CoolProp.CoolProp as CP
        Temperatura = CP.PropsSI("T","P",101325,"Q",0,"SRK::Propane")
        print (Temperatura)
        
* D": Especifica que estamos interessados na densidade.
* "P": Especifica que a primeira entrada é a pressão.
* 101325: Valor da pressão em Pascal (1 atm).
* "Q": Especifica que a segunda entrada é a qualidade do vapor.
* 0: Qualidade do vapor (0 significa líquido saturado).
* "SRK::Propane": Especifica o fluido (Propane) e o modelo de estado (Soave-Redlich-Kwong equation of state - SRK).

#### E para calcular o volume? 

Por definição, O volume é dado por 1/Densidade, então basta substituir T por D para calcular a densiidade na pressão dada

        import CoolProp.CoolProp as CP
        densidade = CP.PropsSI("D","P",101325,"Q",0,"SRK::Propane")
        volume = 1 / densidade
        print (volume)
