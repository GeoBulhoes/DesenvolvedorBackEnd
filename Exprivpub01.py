class Produto:
    # Atributo estático para contar a quantidade de produtos
    qtdProd = 0

    def __init__(self, codigo, preco):
        # Atributos privados
        self.__codigo = codigo
        self.__preco = preco
        # Incrementa o contador estático sempre que um novo produto é criado
        Produto.qtdProd += 1

    # Métodos get para acessar os atributos privados
    def get_codigo(self):
        return self.__codigo

    def get_preco(self):
        return self.__preco

    # Métodos set para modificar os atributos privados
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_preco(self, preco):
        self.__preco = preco

# Testando a classe Produto

# Criando produtos
produto1 = Produto(101, 29.90)
produto2 = Produto(102, 45.50)

# Acessando os atributos dos produtos
print("Produto 1 - Código:", produto1.get_codigo(), "Preço:", produto1.get_preco())
print("Produto 2 - Código:", produto2.get_codigo(), "Preço:", produto2.get_preco())

# Alterando os atributos dos produtos
produto1.set_codigo(201)
produto1.set_preco(39.90)

print("Produto 1 (alterado) - Código:", produto1.get_codigo(), "Preço:", produto1.get_preco())

# Verificando o contador de produtos
print("Quantidade de produtos criados:", Produto.qtdProd)