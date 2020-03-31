def multiplicar():
    print("Ok, vamos multiplicar: ")
    numeros = []

    print("Para parar de multiplicar, clique no '0'!")
    numero = float(input("Entre com um número "))
    # Aqui o usuário pode decidir se ainda deseja fazer algum calculo ou se quer sair
    while numero != 0:
        if type(numero) == float:
            numeros.append(numero)
            numero = float(input("Entre com outro número "))

    resultado = 1
    for numero in numeros:
        resultado *= numero

    print("---> O resultado da multiplicação é: ", resultado, "\n")
