class Pessoa:
    def __init__(self, nome, salario):
        self.salario = salario
        self.nome = nome

def aumento():
    novosalario = Pessoa.salario + Pessoa.salario/100*15
    return novosalario

