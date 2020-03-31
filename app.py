import menu, somar, subtrair, dividir, multiplicar, erro

# Saudação inicial
mensagemIncial = str(input("Olá, digite '0' para sair da calculadora ou qualquer tecla para continuar: "))

# Aqui o usuário pode decidir se ainda deseja fazer algum calculo ou se quer sair
while mensagemIncial != '0':
        menu.menu()

        # Opcoes do Usuario
        opcao = int(input())
        print("Você selecionou a opção: ", opcao, "\n")

        # Estrutura de controle
        if opcao == 1:
                somar.somar()
        elif opcao == 2:
                subtrair.subtrair()
        elif opcao == 3:
                dividir.dividir()
        elif opcao == 4:
                multiplicar.multiplicar()
        else:
                erro.erro()
        mensagemIncial = str(input("Digite 0 para sair ou qualquer tecla para continuar "))
