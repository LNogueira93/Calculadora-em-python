def somar():
    print("Ok, vamos somar: ")
    numeros = []

    print("Para parar de adicionar, clique no '0'!")    
    numero = float(input("Entre com um número "))
    # Aqui o usuário pode decidir se ainda deseja fazer algum calculo ou se quer sair
    while numero != 0:
        if type(numero) == float:
            numeros.append(numero)
            numero = float(input("Entre com outro número "))
    
    print("---> O resultado da soma é: ", sum(numeros), "\n")
