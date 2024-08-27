class Pessoa:
    nome = None
    idade = None

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self, anoatual):
        return anoatual - self.idade
    
pessoa = Pessoa("Pedro", 21)
print(pessoa.getAnoNascimento(2013))
