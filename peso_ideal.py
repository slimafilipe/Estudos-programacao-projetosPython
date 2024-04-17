print("CALCULO DE PESO IDEAL")
alt = eval(input("DIGITE A SUA ALTURA: "))
genero = input("O GENERO É FEMININO OU MASCULINO? ")
ideal_homem = (72.7 * alt) - 58
ideal_mulher = (62.1 * alt) - 44.7
if(genero == 'masculino'):
    print(f'O seu peso ideal é {ideal_homem}')
else:
    print(f'O seu peso ideal é {ideal_mulher}')

