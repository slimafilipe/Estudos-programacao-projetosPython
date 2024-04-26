fat = eval(input("Digite um número "))
def fatorial_interativo(n):
   if((n==0) or (n==1)):
       return  1
   return n*fatorial_interativo(n-1)

print(f"O fatorial de {fat } é {fatorial_interativo(fat)}")