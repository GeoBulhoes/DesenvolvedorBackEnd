# Define a função somaImposto
def somaImposto(taxaImposto, custo):
    # Calcula o valor do imposto
    valor_imposto = custo * (taxaImposto / 100)
    # Adiciona o valor do imposto ao custo original
    custo_final = custo + valor_imposto
    return custo_final

# Solicita ao usuário que insira a taxa de imposto e o custo do item
taxa = float(input("Digite a taxa de imposto sobre vendas (em %): "))
custo_inicial = float(input("Digite o custo do item antes do imposto: R$ "))

# Chama a função e armazena o custo final
custo_com_imposto = somaImposto(taxa, custo_inicial)

# Imprime o custo final do item após a aplicação do imposto
print(f"O custo do item após a aplicação do imposto é: R$ {custo_com_imposto:.2f}")