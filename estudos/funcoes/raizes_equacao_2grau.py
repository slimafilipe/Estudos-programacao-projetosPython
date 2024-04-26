import numpy as np
def calcular_raizes(a,b,c,delta):
    if delta<0:
        resultado = 'A equação não possui raízes nos números reais'
    elif delta == 0:
        x = -b/(2*0)
        resultado = f'A equação possui apenas a raiz: {x}'
    else:
        x1 = (-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.sqrt(delta))/(2*a)
        resultado = f'A equação possui as raízes: {x1}, {x2}'
    return resultado


def entrada_dados():
    coeficiente = quantidade = eval(input("Digite o valor do coeficiente: "))
    return coeficiente

def cal_delta(a,b,c):
    delta = b*b-4*a*c
    return delta

a=entrada_dados()
b=entrada_dados()
c=entrada_dados()

delta=cal_delta(a,b,c)
resultado=calcular_raizes(a,b,c,delta)
print(resultado)