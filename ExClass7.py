class Aluno:
    nome = None
    curso = None
    temposemdormir = None
    
    def __init__(self, nome, curso, temposemdormir):
        self.nome = nome
        self.curso = curso
        self.temposemdormir = temposemdormir
  
    def estudar(self, qtdest):
        return self.temposemdormir + qtdest
    
    def dormir(self, qtdsono):
        return self.temposemdormir - qtdsono
    
Alu = Aluno("Maria", "Python", 20)
print(Alu.estudar(10))
print(Alu.dormir(3))