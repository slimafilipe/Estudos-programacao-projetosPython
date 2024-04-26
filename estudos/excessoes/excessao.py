while True:
    try:
        x = int(input("Digite um valor: "))
        print("Número adicionado com sucesso!")
        break
    except ValueError:
        print("Entre com um número válido. ")

