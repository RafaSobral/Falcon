class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = int(idade)
        self.endereco = endereco

    def exibir_dados(self):
        print('Nome: ' + self.nome)
        print('Idade: ' + str(self.idade))
        print('Endereco: ' + self.endereco)

    def set_dados(self, valor):
        self.endereco = valor
        print('endereco atualizado')


p1 = Pessoa("Rafael",'24','Jovino Duarte')
p1.exibir_dados()
NovoEndereco = input("\nDigite um novo endereco: ")
p1.set_dados(NovoEndereco)
p1.exibir_dados()

