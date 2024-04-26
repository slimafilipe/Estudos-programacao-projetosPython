class Pessoa:
    def __init__(self, nome,ender):
        self.set_nome(nome)
        self.set_ender(ender)
    def set_nome(self, nome):
        self.nome=nome
    def set_ender(self, ender):
        self.ender=ender
    def get_nome(self):
        return self.nome
    def get_ender(self):
        return self.ender

pessoa1 = Pessoa("Filipe", "Rua sem saída")
pessoa2 = Pessoa("Jaiany", "Rua com saída")

print(f'Nome: {pessoa1.get_nome()}, mora no Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, mora no Endreço: {pessoa2.get_ender()}')