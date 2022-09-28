'''
Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %,
a segunda é utilizando o método format e a última é utilizando f strings.
A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo
iremos focar nas 2 últimas.
'''
# METODO FORMAT

nome = "Rafael"
idade = 22
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo {}, tenho {} anos, trabalho como {} e estou aprendendo a linguangem de programação {}".format(nome, idade, profissao, linguagem))

# METODO f-string

nome = "Henrique"
idade = 34
profissao = "pedreiro"

print(f"Olá, me chamo {nome}, tenho {idade} anos, trabalho como {profissao}")

# FORMATANDO STRING COM F-STRING
PI = 3.14159
print(f"valor de PI:{PI:.2f}")
# saida: valor de PI:3.14

print("-"*30)
PI = 3.14159
print(f"valor de PI:{PI:10.2f}") # Foi colocado 10 espaços em branco na frente
# saida: valor de PI:          3.14