# Solicita ao usuário que insira as duas strings
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Calcula o comprimento das strings
tamanho1 = len(string1)
tamanho2 = len(string2)

# Exibe o conteúdo e o comprimento de cada string
print(f"String 1: {string1}")
print(f"Tamanho de \"{string1}\": {tamanho1} caracteres")

print(f"String 2: {string2}")
print(f"Tamanho de \"{string2}\": {tamanho2} caracteres")

# Verifica se os comprimentos das strings são iguais ou diferentes
if tamanho1 == tamanho2:
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

# Verifica se o conteúdo das strings é igual ou diferente
if string1 == string2:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")