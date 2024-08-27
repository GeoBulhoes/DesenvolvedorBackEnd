# Classe Produto
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo       # Código único do produto
        self.nome = nome           # Nome do produto
        self.preco = preco         # Preço do produto

    def __repr__(self):
        return f"Produto(codigo={self.codigo}, nome='{self.nome}', preco={self.preco})"

# Classe GerenciadorProdutos
class GerenciadorProdutos:
    def __init__(self):
        self.produtos = []  # Inicializa uma lista vazia que armazenará os produtos

    def AdicionarProduto(self, produto):
        self.produtos.append(produto)  # Adiciona o produto à lista
        print(f"Produto {produto.nome} adicionado com sucesso.")  # Confirma a adição

    def RemoverProduto(self, codigo):
        produto_removido = None  # Variável para armazenar o produto removido
        for produto in self.produtos:
            if produto.codigo == codigo:  # Verifica se o código do produto corresponde
                produto_removido = produto
                self.produtos.remove(produto)  # Remove o produto da lista
                print(f"Produto {produto.nome} removido com sucesso.")  # Confirma a remoção
                break
        if produto_removido is None:  # Se nenhum produto foi removido
            print(f"Nenhum produto com o código {codigo} foi encontrado.")

    def __repr__(self):
        return f"GerenciadorProdutos(produtos={self.produtos})"  # Representa a lista de produtos

# Exemplo de uso
# Criando alguns produtos
produto1 = Produto(1, "Camiseta", 50.0)
produto2 = Produto(2, "Calça", 100.0)

# Criando o gerenciador de produtos
gerenciador = GerenciadorProdutos()

# Adicionando produtos ao gerenciador
gerenciador.AdicionarProduto(produto1)
gerenciador.AdicionarProduto(produto2)

# Exibindo o estado atual do gerenciador
print(gerenciador)  # Saída: GerenciadorProdutos(produtos=[Produto(codigo=1, nome='Camiseta', preco=50.0), Produto(codigo=2, nome='Calça', preco=100.0)])

# Removendo um produto pelo código
gerenciador.RemoverProduto(1)

# Exibindo o estado atual do gerenciador após a remoção
print(gerenciador)  # Saída: GerenciadorProdutos(produtos=[Produto(codigo=2, nome='Calça', preco=100.0)])