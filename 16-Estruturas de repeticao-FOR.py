# Comando for e a função built-in range
'''
EXEMPLO:
    Receba um número do teclado e exiba os 2 números seguintes
'''
numero = int(input("Digite um número: "))

for i in range(2):
    numero +=1
    print(numero)

print("#"*30)

texto=input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")
print()

print("#"*30)
print("Utiliznado o for junto com o else")

texto= "tttrra"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")

else:
    print()
    print("Executando o fina ldo laço")

