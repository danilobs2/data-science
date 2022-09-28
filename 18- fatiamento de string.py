'''
Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original),
informando inicio (start), fim (stop) e passo (step):
    [start: stop[, step]].
'''

nome = "Fulano de Tal"

print(nome[0])
print("+"*20)

print(nome[:9]) # de 0 ate  8, o indice de  numero 9 não é contado.
print("+"*20)

print(nome[10:]) # Do indice 10 em diante
print("+"*20)

print(nome[3:10]) # Do indice 3 até o indice 9 , o indice de  numero 10 não é contado.
print("+"*20)

print(nome[0:6:2]) # do indice 0 até o indice 5 ,contando de 2 em dois
print("+"*20)

print(nome[:]) # Retorna a String inteira
print("+"*20)

print(nome[::-1]) # Imprime da frente para trás
print("+"*20)

print(nome[-1]) # Exibe a ultima letra da string

