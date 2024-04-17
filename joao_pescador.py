print("***********  PESCARIA DO JOÃO  ***********")
peso_peixe = eval(input("Quantos quilos tem o peixe? "))
permitido = 50
if(peso_peixe > permitido):
    excesso = peso_peixe - permitido
    multa = excesso * 4
    print(f'O peso de {peso_peixe} ultrapassou o valor máximo permitido')
    print(f'Sua multa será de R$ {multa}')
else:
    print(f'O peso de {peso_peixe} está dentro do permitido. Não tem multa a ser cobrada')