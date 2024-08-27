# Inicializa as variáveis para soma e contagem
soma = 0

# Lê 5 números do usuário
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma = numero + soma

# Calcula a média
media = soma / 5

# Imprime a soma e a média
print("A soma dos 5 números é:", soma)
print("A média dos 5 números é:", media)