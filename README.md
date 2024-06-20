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

A primeira coisa que faremos é **instalar as bibliotecas** , usaremos `sympy` para trabalhar com símbolos
Basta abrir o promt de comando de seu computador e digitar pip install (nome da biblioteca) - **sem parenteses**
Lembremos que para importar uma biblioteca é necessário utilizar o comando `pip install + nomes de bibliotecas´.

Em seguida para importa-las, é necessário utilizar o comando `import + nomes de bibliotecas`. logo no início de seu projeto.

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

