print("Conhecendo os operadores lógicos")

# Operador E
saldo = 1000
saque = 200
limite = 100

var = saldo >= saque and saque <= limite
print(var)

# Operador OU
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque or saque <= limite)

# Operador negação
contatos_emergencia = [] # Lista vazia em python é igual a zero, mas por conta da negação ela se torna True
print(not 1000 > 1001)

print(not "saque 1001") # A string possui valor, mas a negação a torna falso

var = not "" # A string não contém valor mas a negação a torna verdadeira
print(var)

# Parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

var = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(var)
