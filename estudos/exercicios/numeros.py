
inteiro1 = eval(input("DIGITE O PRIMEIRO NÚMERO INTEIRO: "))
inteiro2 = eval(input("DIGITE O SEUGUNDO NÚMERO INTEIRO: "))
real = eval(input("DIGITE UM NÚMERO REAL: "))
produto = (inteiro1 ** 2) + (inteiro2 / 2)
soma = (inteiro1 * 3) + real
cubo = real ** 3

print(f'O produto do dobro do primeiro número com a metade do segundo é {produto}')
print(f'A soma do triplo do primeiro com o terceiro número é {soma}')
print(f'O terceiro elevado ao cubo é {cubo}')