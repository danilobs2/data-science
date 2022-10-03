'''
# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split()

# TODO: 
'''

'''
Desafio
Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L.
Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda.
Para efetuar o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h.
Assim, você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários para a viagem 
que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.

Entrada
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.
'''
# Calcule a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal:

KM_LITRO = 12

valores = input().split()

tempoGasto = float(valores[0])
velocidadeMedia = float(valores[1])

distancia = tempoGasto*velocidadeMedia
consumo = distancia / 12

print(f"{consumo:.3f}")
