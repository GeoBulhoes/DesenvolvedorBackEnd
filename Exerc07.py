# Solicita ao usuário a temperatura em graus Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Converte Fahrenheit para Celsius usando a fórmula C = 5 * ((F-32) / 9)
celsius = 5 * ((fahrenheit - 32) / 9)

# Imprime o resultado
print("A temperatura em graus Celsius é:", celsius)