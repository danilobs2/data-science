print("Operadores de identidade")
# is
'''
O que são?
São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.
'''

curso = "Curso de Python"
nome_curso = curso # A variavel nome_curso recebe o valor da variavel curso
saldo, limite = 200, 200

var = curso is nome_curso
print(var)

print(saldo is limite)
