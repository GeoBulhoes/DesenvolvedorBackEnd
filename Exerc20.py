# Define a função que retorna 'P' para valores positivos e 'N' para zero ou negativos
def verifica_positivo_negativo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Chama a função e armazena o resultado
resultado = verifica_positivo_negativo(numero)

# Imprime o resultado
print(f"O valor retornado pela função é: '{resultado}'")