opcao= -1

while opcao != 0:
    print("Digite [1]Sacar - [2]Extrato - [0]Sair")
    opcao=int(input("Opção: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Imprimindo o extrato...")
    else:
        print("Saindo")
