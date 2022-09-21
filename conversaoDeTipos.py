print("CONVERTENDO INTEIRO PARA FLOAT")

valor = 10
print("Valor inteiro: "+str(valor))

valor = float(valor)
print("valor convertido para float: "+str(valor))

print("valor convertido para float: "+str(valor // 2))

print(10 / 2)
print(10 // 2)

print("*"*20)
print("CONVERTENDO FLOAT PARA INTEIRO")

valor1 = 10.30
print(valor1)

valor1 = int(valor1)
print(valor1)

print("*"*20)
print("CONVERTENDO NÚMERO PARA string")

valor2 = 10.40
idade = 27

print(str(valor2))
print("Idade: {} e valor2: {}".format(idade, valor2))
# OU
texto = f"idade: {idade} e valor2: {valor2}"
print(texto)

print("*"*20)
print("CONVERTENDO STRING PARA NÚMERO")

valor3 = "10.50"
idade = "28"
print("valor3:",type(valor3))
print("idade:",type(idade))

print(float(valor3))
print(int(idade))

