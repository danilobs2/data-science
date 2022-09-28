print("Conhecendo metodos uteis da classe string\n")

palavra = "PythoN"

print("Exibindo o texto em MAISCULO")
print(palavra.upper())
print()
print("Exibindo o texto em Minusculo")
print(palavra.lower())
print()
print("Exibindo a primeira letra em MAISCULO")
print(palavra.title())
print()

print("+"*27)

# ELIMINANDO ESPAÇOS EM BRANCO
palavra1 = "  Python  "

print("strip remove os espaços no início e no final da string")
var = palavra1.strip()
print("O",var,"não é uma cobra")
print("+"*27)
print("lstrip remove os espaços à esquerda da string")
var = palavra1.lstrip()
print("O",var,"não é uma cobra")
print("+"*27)
print("lstrip remove os espaços à direita da string")
var = palavra1.rstrip()
print("O",var,"não é uma cobra")
print("+"*27)

# JUNÇÕES E CENTRALIZAÇÃO
texto = "GitHub"

print(texto.center(10,"#")) # .center(), centrraliza o texto e acrescenta 4 #, contabilizando o total de 10 caracteres.
      #saida: ##GitHub##

print(".".join(texto))
      #saida: "G.i.t.H.u.b"