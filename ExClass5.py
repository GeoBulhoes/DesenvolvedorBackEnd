class Livro:
    nome = None
    qtdPagina = None
    autor = None
    preco = None
    
    def __init__(self, nome, qtdPagina, autor, preco):
        self.nome = nome
        self.qtdPagina = qtdPagina
        self.autor = autor
        self.preco = preco

    def getpreco(self): #Todo método tem um self
        return self.preco
    
    def setpreco(self, val):
        return self.preco + val
    
liv01 = Livro("Maria", 500, "Aaron Ross", 100)
print(liv01.setpreco(10))