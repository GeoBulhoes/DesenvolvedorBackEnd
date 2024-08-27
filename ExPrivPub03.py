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

    def PrecoTotal(self, listaCodigos):
        total = 0.0  # Inicializa o total com 0
        for codigo in listaCodigos:
            for produto in self.produtos:
                if produto.codigo == codigo:  # Se o código do produto estiver na lista
                    total += produto.preco  # Adiciona o preço ao total
                    break  # Interrompe a busca após encontrar o produto
        return total  # Retorna a soma dos preços

    def __repr__(self):
        return f"GerenciadorProdutos(produtos={self.produtos})"  # Representa a lista de produtos

# Exemplo de uso
# Criando alguns produtos
produto1 = Produto(1, "Camiseta", 50.0)
produto2 = Produto(2, "Calça", 100.0)
produto3 = Produto(3, "Tênis", 200.0)

# Criando o gerenciador de produtos
gerenciador = GerenciadorProdutos()

# Adicionando produtos ao gerenciador
gerenciador.AdicionarProduto(produto1)
gerenciador.AdicionarProduto(produto2)
gerenciador.AdicionarProduto(produto3)

# Calculando o preço total dos produtos com códigos 1 e 3
total = gerenciador.PrecoTotal([1, 3])
print(f"Preço total dos produtos com códigos 1 e 3: {total}")  # Saída: Preço total dos produtos com códigos 1 e 3: 250.0