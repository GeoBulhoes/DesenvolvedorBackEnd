class Funcionario:
    nome = None
    salario = None
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumento(self, aum): #Todo método tem um self
        return self.salario * ((aum/100) + 1)
    
fun01 = Funcionario("Maria", 1500)
print(fun01.aumento(10))


