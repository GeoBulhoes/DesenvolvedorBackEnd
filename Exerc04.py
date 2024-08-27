import math

# Solicita ao usuário que insira o valor do raio
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo (A = πr²)
area = math.pi * (raio ** 2)

# Imprime o resultado
print("A área do círculo com raio", raio, "é:", area)