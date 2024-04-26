print("****** CALCULO DE HORAS TRABALHADAS E DESCONTOS NO SALARIO ******")

valor_horas = eval(input("QUANTO VOCÊ GANHA POR HORA? "))
horas_trabalhadas = eval(input("QUANTAS HORAS FORAM TRABALHADAS? "))
salario_bruto = horas_trabalhadas * valor_horas

print(f'SEU SÁLARIO BRUTO ESSE MÊS É DE {salario_bruto}')

ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100

con_ir = input("CONTRIBUI COM IMPOSTO DE RENDA? ")
con_sind = input("CONTRIBUI COM SINDICATO? ")
if con_ir == "s" and con_sind == "s":
    desconto = ir + inss + sindicato
    salario_liquido = salario_bruto - desconto
    print(f'SEU SÁLARIO LIQUIDO  É DE {salario_liquido}')
else:
    salario_liquido = salario_bruto - inss
    print(f'SEU SÁLARIO LIQUIDO COM DESCONTO DE {inss} DO INSS É DE {salario_liquido}')

