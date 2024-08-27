class Aluno:
    def __init__(self, nome, idade, matricula, curso):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.curso = curso

    def falar(self):
        return "Eu estou falando...."

aluno = Aluno("Maria", 18, "12348957849", "Python para Backend")
print(aluno.falar())

    
