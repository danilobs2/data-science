print("Estruturas Condicionais")

'''
O que são?
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões 
lógicas são atendidas.
'''
print("+" * 25)
print("Trabalhando com if")

saldo = 2000
saque = float(input("Digite o valor do saque: "))

if saque <= saldo:
    print("Realizando saque")

if saque > saldo:
    print("Saldo insuficiente")

print("+" * 25)
print("trabalhando com if/else")
saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

print("+" * 25)
print("trabalhando com elif")

print("Digite [1]Sacar | [2]Extrato")
opcao = int(input("Opcao: "))

if opcao == 1:
    valor = float(input("Digite a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato!")
else:
    print("Opção inválida")

print("+" * 25)
print("if aninhado")
conta_normal = False
cheque_especial = False
conta_universitaria = False
saldo = -1

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")

print("+" * 25)
print("if ternário")

'''
O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a
primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão
lógica e a terceira parte é o retorno caso a expressão não seja atendida.
'''

pedido = "Aprovado" if saldo >= saque else "Negado"
print(pedido, "ao realizar o saque")
