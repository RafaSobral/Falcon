class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome 
        self.salario = float(salario) 

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus 

    def calcular_salario(self):
        self.total = self.salario + self.bonus 
        print(f'Total: {self.total}')
    
    def exibir_dados(self):
        print(f'Nome: {self.nome}\nSalario: {self.salario}\nBonus:{self.bonus}')


func1 = Gerente('Rafael',2232.50,500)
func1.exibir_dados()
func1.calcular_salario()


        