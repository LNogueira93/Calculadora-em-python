def dividir():
    print("Ok, vamos dividir: ")
    numeros = []

    print("Para parar de dividir, clique no '0'!")
    numero = float(input("Entre com um número "))
    # Aqui o usuário pode decidir se ainda deseja fazer algum calculo ou se quer sair
    while numero != 0:
        if type(numero) == float:
            numeros.append(numero)
            numero = float(input("Entre com outro número "))

    primeiro = numeros[0]
    removed = numeros.remove(primeiro)
    for numero in numeros:
        primeiro /= numero

    print("---> O resultado da divisão é: ", primeiro, "\n")
